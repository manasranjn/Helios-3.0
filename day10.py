class Car:
    def __init__(self, price, model, year):
        self.price = price
        self.model = model
        self.year = year

    def display(self):
        print("Price:", self.price)
        print("Model:", self.model)
        print("Year:", self.year)

    def start(self):
        print("Starting the car...")


class BMW(Car):
    def stop(self):
        print("Stopping the car...")

    def display(self):
        print(f"Price: {self.price}, Model: {self.model}, Year: {self.year}")

m4 = BMW(1000000, "M4", 2022)
m4.display()
# m4.start()
# m4.stop()

car = Car(1000000, "M4", 2022)
car.display()
# car.start()