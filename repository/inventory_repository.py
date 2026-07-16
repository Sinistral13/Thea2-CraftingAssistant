from models import Inventory


class InventoryRepository:

    def __init__(self, session):
        self.session = session

    def _cursor(self):
        return self.session.connection.cursor()

    def _map(self, row):
        inventory_id = (Inventory, row[0])

        if inventory_id in self.session.identity_map:
            return self.session.identity_map[inventory_id]

        inventory = Inventory(
            id=row[0],
            player=row[1],
            material=row[2],
            amount=row[3]
        )

        self.session.identity_map[inventory_id] = inventory

        return inventory

    def get_by_id(self, inventory_id):
        sql = "SELECT * FROM inventory WHERE id = %s"

        cursor = self._cursor()
        cursor.execute(sql, (inventory_id,))
        row = cursor.fetchone()

        return self._map(row) if row else None

    def get_by_player_and_material(self, player, material):
        sql = """SELECT * FROM inventory
                 WHERE player = %s AND material = %s
              """

        cursor = self._cursor()
        cursor.execute(sql, (player, material))
        row = cursor.fetchone()

        return self._map(row) if row else None

    def get_all(self):
        cursor = self._cursor()
        cursor.execute("SELECT * FROM inventory")

        return [self._map(row) for row in cursor.fetchall()]
    

    def get_by_player(self, player):
        sql = "SELECT * FROM inventory WHERE player = %s"

        cursor = self._cursor()
        cursor.execute(sql, (player,))

        return [self._map(row) for row in cursor.fetchall()]
    

    def insert(self, inventory):
        sql = """
            INSERT INTO inventory
            (
                player,
                material,
                amount
            )
            VALUES (%s, %s, %s)
            RETURNING id
        """

        cursor = self._cursor()
        cursor.execute(sql, (
            inventory.player,
            inventory.material,
            inventory.amount
        ))

        new_id = cursor.fetchone()[0]
        self.session.connection.commit()

        return new_id
    

    def delete_by_id(self, inventory_id):
        sql = "DELETE FROM inventory WHERE id = %s"

        cursor = self._cursor()
        cursor.execute(sql, (inventory_id,))
        self.session.connection.commit()

        inventory_key = (Inventory, inventory_id)
        self.session.identity_map.pop(inventory_key, None)
        