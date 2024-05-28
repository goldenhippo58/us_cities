# US Cities Library

This library provides information about US cities.

## Installation

```bash
pip install us_cities


from us_cities import city_info

city = city_info.get_city_info('Los Angeles')
print(city)

cities_in_california = city_info.get_cities_by_state('California')
print(cities_in_california)
