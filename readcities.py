from cities import City

with open('cities.txt') as f:
    Cities = [City(i) for i in f.read().split('\n')]