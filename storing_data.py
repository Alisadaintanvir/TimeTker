import json
from datetime import datetime

now = datetime.now()
date = now.strftime("%d/%m/%Y")


class StoringData:
    def __init__(self):
        self.date = date

    def store_counter_value(self, value):
        new_entry = {
            "date": self.date,
            "value": value
        }

        existing_data = []

        try:
            with open("timer_data.json", "r") as data_file:
                existing_data = json.load(data_file)
        except FileNotFoundError:
            pass

        for entry in existing_data:
            if entry['date'] == self.date:
                entry['value'] += value
                break
        else:
            existing_data.append(new_entry)
        with open("timer_data.json", "w") as json_file:
            json.dump(existing_data, json_file)

    def fetch_data(self):
        try:
            with open("timer_data.json") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return []
