import os
import pickle

class Database:
    FILE_NAME = "students.data"

    @staticmethod
    def load_data():
        if not os.path.exists(Database.FILE_NAME):
            return []
        try:
            with open(Database.FILE_NAME, "rb") as f:
                return pickle.load(f)
        except (pickle.UnpicklingError, EOFError, Exception) as e:
            print(f"[Error] Failed to load data: {e}")
            return []

    @staticmethod
    def save_data(data):
        try:
            with open(Database.FILE_NAME, "wb") as f:
                pickle.dump(data, f)
            print(f"[Database] Saved {len(data)} records.")
        except Exception as e:
            print(f"[Error] Failed to save data: {e}")

    @staticmethod
    def clear_data():
        try:
            with open(Database.FILE_NAME, "wb") as f:
                pickle.dump([], f)
            print("[Database] Data cleared.")
        except Exception as e:
            print(f"[Error] Failed to clear data: {e}")
