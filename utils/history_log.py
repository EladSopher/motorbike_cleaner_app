import json
import os
from datetime import datetime
from kivy.utils import platform

class HistoryLog:
    def __init__(self):
        self.entries = []
        self.log_file = self._get_log_path()  # ✅ use this consistently
        self._load_entries()

    def _get_log_path(self):
        if platform == 'android':
            from android.storage import app_storage_path
            return os.path.join(app_storage_path(), "cleaning_log.json")
        else:
            return os.path.join(os.path.dirname(__file__), "cleaning_log.json")

    def _load_entries(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, "r", encoding="utf-8") as file:
                self.entries = json.load(file)
        else:
            self.entries = []

    def _save_entries(self):
        with open(self.log_file, "w", encoding="utf-8") as file:
            json.dump(self.entries, file, indent=2)

    def add_entry(self, action_type="cleaning"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_entry = {
            "timestamp": timestamp,
            "action": action_type
        }
        self.entries.append(new_entry)
        self._save_entries()

    def get_entries(self):
        return self.entries

    def export_to_csv(self, filename="history_export.csv"):
        import csv

        export_path = os.path.join(os.path.dirname(__file__), filename)
        with open(export_path, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Timestamp", "Action"])  # Header
            for entry in self.entries:
                writer.writerow([entry["timestamp"], entry["action"]])

        return export_path  # to display on screen

    def clear_history(self):
        self.entries = []
        with open(self.log_file, 'w') as f:
            json.dump([], f)