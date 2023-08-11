
from movieweb_app.datamanager.json_data_manager import JSONDataManager
# from csv_data_manager import CSVDataManager (if implemented)

def main():
    json_manager = JSONDataManager('data.json')
    # csv_manager = CSVDataManager('data.csv')

    # Example usage
    all_users = json_manager.get_all_users()
    print(all_users)

    user_movies = json_manager.get_user_movies(1)
    print(user_movies)

if __name__ == "__main__":
    main()
