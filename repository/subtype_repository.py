class MaterialRepository:

    def __init__(self, connection):
        self.connection = connection

    def get_by_id(self, material_id):
        sql = "SELECT * FROM material where id = ?"

        cursor = self.connection.cursor()
        cursor.execute(sql, (material_id,))
        row = cursor.fetchone()

    return Material(*row) if row else None


    def get_by_name(self, name):
        sql = "SELECT * FROM material WHERE name = ?"

        cursor = self.connection.cursor()
        cursor.execute(sql, (name,))
        row = cursor.fetchone()

        return Material(*row) if row else None
    

    def get_all(self):
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM material")

        return [Material(*row) for row in cur.fetchall()]
    

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
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            RETURNING id
        """

        cur = self.connection.cursor()
        cur.execute(sql, (
            material.name,
            material.essence1,
            material.amount1,
            material.essence2,
            material.amount2,
            material.subtype,
            material.composite,
            material.tier,
        ))

        new_id = cur.fetchone()[0]
        self.connection.commit()

        return new_id