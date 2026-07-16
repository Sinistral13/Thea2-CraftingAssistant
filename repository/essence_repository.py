from models import Essence

class EssenceRepository:

    def __init__(self, session):
        self.session = session
        
    def _cursor(self):
        return self.session.connection.cursor()
    
    def _map(self, row):
        essence_id = (Essence, row[0])

        if essence_id in self.session.identity_map:
            return self.session.identity_map[essence_id]

        essence = Essence(
            id=row[0],
            name=row[1])

        self.session.identity_map[essence_id] = essence

        return essence

        
    def get_by_id(self, essence_id):
        sql = "SELECT * FROM essence where id = %s"
        
        cursor = self._cursor()
        cursor.execute(sql, (essence_id,))
        row = cursor.fetchone()

        return self._map(row) if row else None


    def get_by_name(self, name):
        sql = "SELECT * FROM essence WHERE name = %s"

        cursor = self._cursor()
        cursor.execute(sql, (name,))
        row = cursor.fetchone()

        return self._map(row) if row else None
    

    def get_all(self):
        cursor = self._cursor()
        cursor.execute("SELECT * FROM essence")

        return [self._map(row) for row in cursor.fetchall()]
    

    def insert(self, essence):
        sql = """
            INSERT INTO essence
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
        sql = "DELETE FROM essence WHERE id = %s"

        cursor = self._cursor()
        cursor.execute(sql, (essence_id,))
        self.session.connection.commit()

        my_essence = (Essence, essence_id)
        self.session.identity_map.pop(my_essence, None)
