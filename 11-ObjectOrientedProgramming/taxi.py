class TaxiRide:
    def __init__(self, rate_per_km, distance, fare):
        self.rate_per_km = rate_per_km
        self.distance = distance
        self.fare = fare

    def calculate_fare(self):
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f'{self.rate_per_km} {self.distance} {self.fare}')


def main():
    ride1 = TaxiRide(40, 23, 13)
    ride2 = TaxiRide(50, 12, 9)

    ride1.calculate_fare()
    ride1.print_receipt()

    ride2.calculate_fare()
    ride2.print_receipt()


if __name__ == "__main__":
    main()
