import csv
import json

class JsonToCsvAdapter:
    @staticmethod
    def convert(json_data, csv_filename):
        data = json.loads(json_data)
        keys = data[0].keys()

        with open(csv_filename, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

# Приклад з уроку
json_example = '[{"Name": "Pavlo", "Age": 31, "City": "Kyiv"}, {"Name": "Alice", "Age": 25, "City": "San Francisco"}]'
JsonToCsvAdapter.convert(json_example, 'example.csv')
