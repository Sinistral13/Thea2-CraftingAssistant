from models import Material

class MaterialRepository:

    def __init__(self, session):
        self.session = session
        
    def _cursor(self):
        return self.session.connection.cursor()
    
    def _map(self, row):
        material_id = (Material, row[0])

        if material_id in self.session.identity_map:
            return self.session.identity_map[material_id]

        material = Material(
            id=row[0],
            name=row[1],
            essence1_id=row[2],
            amount1=row[3],
            essence2_id=row[4],
            amount2=row[5],
            subtype_id=row[6],
            composite=row[7],
            tier=row[8])

        self.session.identity_map[material_id] = material

        return material

        
    def get_by_id(self, material_id):
        sql = "SELECT * FROM material where id = %s"
        
        cursor = self._cursor()
        cursor.execute(sql, (material_id,))
        row = cursor.fetchone()

        return self._map(row) if row else None


    def get_by_name(self, name):
        sql = "SELECT * FROM material WHERE name = %s"

        cursor = self._cursor()
        cursor.execute(sql, (name,))
        row = cursor.fetchone()

        return self._map(row) if row else None
    

    def get_all(self):
        cursor = self._cursor()
        cursor.execute("SELECT * FROM material")

        return [self._map(row) for row in cursor.fetchall()]
    

    def insert(self, material):
        sql = """
            INSERT INTO material
            (
                name,
                essence1, amount1,
                essence2, amount2,
                subtype,
                composite,
                tier
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """

        cursor = self._cursor()
        cursor.execute(sql, (
            material.name,
            material.essence1_id,
            material.amount1,
            material.essence2_id,
            material.amount2,
            material.subtype_id,
            material.composite,
            material.tier
        ))

        new_id = cursor.fetchone()[0]
        self.session.connection.commit()

        return new_id
    
    
    def delete_by_id(self, material_id):
        sql = "DELETE FROM material WHERE id = %s"

        cursor = self._cursor()
        cursor.execute(sql, (material_id,))
        self.session.connection.commit()

        my_material = (Material, material_id)
        self.session.identity_map.pop(my_material, None)