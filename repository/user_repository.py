from models import AppUser


class UserRepository:

    def __init__(self, session):
        self.session = session
        
    def _cursor(self):
        return self.session.connection.cursor()
    
    def _map(self, row):
        user_key = (AppUser, row[0])

        if user_key in self.session.identity_map:
            return self.session.identity_map[user_key]

        app_user = AppUser(
            username=row[0],
            password=row[1]
        )

        self.session.identity_map[user_key] = app_user

        return app_user


    def get_by_name(self, name):
        sql = """
            SELECT username, password
            FROM usertable
            WHERE username = %s
        """

        cursor = self._cursor()
        cursor.execute(sql, (name,))
        row = cursor.fetchone()

        return self._map(row) if row else None


    def get_all(self):
        cursor = self._cursor()
        cursor.execute(
            "SELECT username, password FROM usertable"
        )

        return [self._map(row) for row in cursor.fetchall()]


    def insert(self, app_user):
        sql = """
            INSERT INTO usertable
            (
                username,
                password
            )
            VALUES (%s, %s)
        """

        cursor = self._cursor()
        cursor.execute(
            sql,
            (
                app_user.username,
                app_user.password
            )
        )

        self.session.connection.commit()

        return app_user.username


    def delete_by_name(self, username):
        sql = """
            DELETE FROM usertable
            WHERE username = %s
        """

        cursor = self._cursor()
        cursor.execute(sql, (username,))
        self.session.connection.commit()

        user_key = (AppUser, username)
        self.session.identity_map.pop(user_key, None)