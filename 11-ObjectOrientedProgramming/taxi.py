class TaxiRide:
    def __init__(self, rate_per_km, distance, fare):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = distance
        self.fare = fare

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self, rate_per_km, distance, fare):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = distance
        self.fare = fare

ride1 = TaxiRide(40, 23, 13)
ride1 = TaxiRide(50, 12, 9)


def main():
    # your program
    ...
    ...
    ...

if __name__ == "__main__":
    main()
