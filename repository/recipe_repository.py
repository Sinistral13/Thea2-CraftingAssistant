from models import Recipe

class RecipeRepository:

    def __init__(self, session):
        self.session = session
        
    def _cursor(self):
        return self.session.connection.cursor()
    
    def _map(self, row):
        recipe_id = (Recipe, row[0])

        if recipe_id in self.session.identity_map:
            return self.session.identity_map[recipe_id]

        recipe = Recipe(
            id=row[0],
            name=row[1],
            primary_amount1=row[2],
            primary_essence_id1=row[3],
            primary_amount2=row[4],
            primary_essence_id2=row[5],
            primary_amount3=row[6],
            primary_essence_id3=row[7],
            primary_amount4=row[8],
            primary_essence_id4=row[9],
            secondary_amount1=row[10],
            secondary_essence_id1=row[11],
            secondary_amount2=row[12],
            secondary_essence_id2=row[13],
            secondary_amount3=row[14],
            secondary_essence_id3=row[15],
            secondary_amount4=row[16],
            secondary_essence_id4=row[17])
            
        self.session.identity_map[recipe_id] = recipe

        return recipe

        
    def get_by_id(self, recipe_id):
        sql = "SELECT * FROM recipe where id = %s"
        
        cursor = self._cursor()
        cursor.execute(sql, (recipe_id,))
        row = cursor.fetchone()

        return self._map(row) if row else None


    def get_by_name(self, name):
        sql = "SELECT * FROM recipe WHERE name = %s"

        cursor = self._cursor()
        cursor.execute(sql, (name,))
        row = cursor.fetchone()

        return self._map(row) if row else None
    

    def get_all(self):
        cursor = self._cursor()
        cursor.execute("SELECT * FROM recipe")

        return [self._map(row) for row in cursor.fetchall()]
    

    def insert(self, recipe):
        sql = """
            INSERT INTO recipe
            (
                name,
                primary_amount1, primary_essence1,
                primary_amount2, primary_essence2,
                primary_amount3, primary_essence3,
                primary_amount4, primary_essence4,
                secondary_amount1, secondary_essence1,
                secondary_amount2, secondary_essence2,
                secondary_amount3, secondary_essence3,
                secondary_amount4, secondary_essence4
            )
            VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """

        cursor = self._cursor()
        cursor.execute(sql, (
            recipe.name,
            recipe.primary_amount1,
            recipe.primary_essence_id1,
            recipe.primary_amount2,
            recipe.primary_essence_id2,
            recipe.primary_amount3,
            recipe.primary_essence_id3,
            recipe.primary_amount4,
            recipe.primary_essence_id4,
            recipe.secondary_amount1,
            recipe.secondary_essence_id1,
            recipe.secondary_amount2,
            recipe.secondary_essence_id2,
            recipe.secondary_amount3,
            recipe.secondary_essence_id3,
            recipe.secondary_amount4,
            recipe.secondary_essence_id4
        ))

        new_id = cursor.fetchone()[0]
        self.session.connection.commit()

        return new_id
    
    def delete_by_id(self, recipe_id):
        sql = "DELETE FROM recipe WHERE id = %s"

        cursor = self._cursor()
        cursor.execute(sql, (recipe_id,))
        self.session.connection.commit()

        my_recipe = (Recipe, recipe_id)
        self.session.identity_map.pop(my_recipe, None)
        