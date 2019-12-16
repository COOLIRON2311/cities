from cities import City

with open('ci.txt') as f:
    Cities = [City(i) for i in f.read().split('\n')]
print(Cities)