import csv
import os

class CityInfo:
    def __init__(self):
        self.data = []
        self.load_data()

    def load_data(self):
        module_path = os.path.dirname(__file__)
        data_path = os.path.join(module_path, 'data.csv')
        with open(data_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.data.append(row)

    def get_city_info(self, city_name):
        for city in self.data:
            if city['city'].lower() == city_name.lower():
                return city
        return None

    def get_cities_by_state(self, state_name):
        cities = [city for city in self.data if city['state_name'].lower() == state_name.lower()]
        return cities

city_info = CityInfo()
