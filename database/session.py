from repository import MaterialRepository
from repository import EssenceRepository
from repository import SubtypeRepository
from repository import RecipeRepository
from repository import UserRepository


class Session:

    def __init__(self, database):

        self.connection = database.connection
        self.identity_map = {}

        self.materials = MaterialRepository(self)
        self.essences = EssenceRepository(self)
        self.subtypes = SubtypeRepository(self)
        self.recipes = RecipeRepository(self)
        self.users = UserRepository(self)