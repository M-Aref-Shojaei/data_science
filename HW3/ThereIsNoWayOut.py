# this code has been programmed by Aref
# github.com/M-Aref-Shojaei

def NoWay(pathes: list, cities: set) -> str:

    for path in pathes:
        cities.remove(path[0])

    return cities.pop()


def listOfCities(pathes: list) -> set:
    cities = set()
    for path in pathes:
        cities.add(path[0])
        cities.add(path[1])
    return cities


ways = input(
    "Enter the pathes(please split the path with ',' and pathes with space ): ").split()

pathes = []

for way in ways:
    pathes.append(way.split(','))

print(NoWay(pathes, listOfCities(pathes)))
