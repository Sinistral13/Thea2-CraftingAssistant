from models import Material

class SubtypeRepository:

    def __init__(self, session):
        self.session = session
        
    def _cursor(self):
        return self.session.connection.cursor()
    
    def _map(self, row):
        subtype_id = (Essence, row[0])

        if subtype_id in self.session.identity_map:
            return self.session.identity_map[subtype_id]

        subtype = Subtype(
            id=row[0],
            name=row[1])

        self.session.identity_map[subtype_id] = subtype

        return subtype

        
    def get_by_id(self, essence_id):
        sql = "SELECT * FROM subtype where id = ?"
        
        cursor = self._cursor()
        cursor.execute(sql, (essence_id,))
        row = cursor.fetchone()

        return self._map(row) if row else None


    def get_by_name(self, name):
        sql = "SELECT * FROM subtype WHERE name = ?"

        cursor = self._cursor()
        cursor.execute(sql, (name,))
        row = cursor.fetchone()

        return self._map(row) if row else None
    

    def get_all(self):
        cursor = self._cursor()
        cursor.execute("SELECT * FROM subtype")

        return [self._map(row) for row in cursor.fetchall()]
    

    def insert(self, essence):
        sql = """
            INSERT INTO subtype
            (
                name
            )
            VALUES (?)
            RETURNING id
        """

        cursor = self._cursor()
        cursor.execute(sql, (essence.name))

        new_id = cursor.fetchone()[0]
        self.session.connection.commit()

        return new_id
    
    def delete_by_id(self, subtype_id):
        sql = "DELETE FROM subtype WHERE id = ?"

        cursor = self._cursor()
        cursor.execute(sql, (subtype_id,))
        self.session.connection.commit()

        my_subtype = (Subtype, subtype_id)
        self.session.identity_map.pop(my_subtype, None)
