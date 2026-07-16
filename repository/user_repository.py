from models import Material

class UserRepository:

    def __init__(self, session):
        self.session = session
        
    def _cursor(self):
        return self.session.connection.cursor()
    
    def _map(self, row):
        user_name = (AppUser, row[0])

        if user_name in self.session.identity_map:
            return self.session.identity_map[user_name]

        app_user = AppUser(
            user_name=row[0],
            password=row[1])

        self.session.identity_map[user_name] = essence

        return essence


    def get_by_name(self, name):
        sql = "SELECT * FROM usertable WHERE name = %s"

        cursor = self._cursor()
        cursor.execute(sql, (name,))
        row = cursor.fetchone()

        return self._map(row) if row else None
    

    def get_all(self):
        cursor = self._cursor()
        cursor.execute("SELECT * FROM usertable")

        return [self._map(row) for row in cursor.fetchall()]
    

    def insert(self, essence):
        sql = """
            INSERT INTO usertable
            (
                name
            )
            VALUES (%s)
            RETURNING id
        """

        cursor = self._cursor()
        cursor.execute(sql, (essence.name))

        new_id = cursor.fetchone()[0]
        self.session.connection.commit()

        return new_id
    
    
    def delete_by_id(self, essence_id):
        sql = "DELETE FROM usertable WHERE id = %s"

        cursor = self._cursor()
        cursor.execute(sql, (essence_id,))
        self.session.connection.commit()

        my_essence = (Essence, essence_id)
        self.session.identity_map.pop(my_essence, None)
