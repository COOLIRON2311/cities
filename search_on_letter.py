from cities import City

def search(c, arr):
    s = None
    for city in arr:
        if city.first == c.upper():
            s = city
            break
    return s
