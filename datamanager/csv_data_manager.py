from movieweb_app.datamanager.data_manager_interface import DataManagerInterface

class CSVDataManager(DataManagerInterface):
    def __init__(self, filename):
        self.filename = filename

    def get_all_users(self):
        # Implement CSV data retrieval
        pass

    def get_user_movies(self, user_id):
        # Implement CSV data retrieval
        pass
