# CPE 202 Lab 0

# represents a location using name, latitude and longitude
class Location:
    def __init__(self, name, lat, lon):
        self.name = name  # string for name of location
        self.lat = round(lat, 3)  # latitude in degrees (float)
        self.lon = round(lon, 3)  # longitude in degrees (float)

    def __repr__(self):
        return f'Location(\'{self.name}\', {self.lat}, {self.lon})'  # return Location class information in a string

    def __eq__(self, other):
        return type(other) == Location and self.name == other.name and round(self.lat, 3) == round(other.lat, 3) and round(self.lon, 3) == round(other.lon, 3)


# ADD BOILERPLATE HERE (__eq__ and __repr__ functions)

# 100% Code coverage NOT required due to the main function
def main():
    loc1 = Location("SLO", 35.3, -120.7)
    loc2 = Location("Paris", 48.9, 2.4)
    loc3 = Location("SLO", 35.3, -120.7)
    loc4 = loc1

    print("Location 1:", loc1)
    print("Location 2:", loc2)
    print("Location 3:", loc3)
    print("Location 4:", loc4)

    # printing boolean values for whether certain locations are the same
    print("\nLocation 1 equals Location 2:", loc1 == loc2)
    print("Location 1 equals Location 3:", loc1 == loc3)
    print("Location 1 equals Location 4:", loc1 == loc4)

    locations = [loc1, loc2]

    # print boolean values for whether certain locations are in the list
    print(loc1 in locations)
    print(loc2 in locations)
    print(loc3 in locations)
    print(loc4 in locations)


if __name__ == "__main__":
    main()
