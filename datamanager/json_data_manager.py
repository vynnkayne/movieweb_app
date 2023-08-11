import json
from movieweb_app.datamanager.data_manager_interface import DataManagerInterface

class JSONDataManager(DataManagerInterface):
    def __init__(self, filename):
        self.filename = filename

    def get_all_users(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
            return data

    def get_user_movies(self, user_id):
        with open(self.filename, 'r') as file:
            data = json.load(file)
            user = next((user for user in data if user['id'] == user_id), None)
            if user:
                return user.get('movies', [])
            return []

