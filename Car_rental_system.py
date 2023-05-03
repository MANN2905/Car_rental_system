class Car:
    def __init__(self, company, model,location):
        self.company = company
        self.model = model
        self.is_rented = False
        self.location = location

    def __str__(self):
        return f"{self.company} {self.model} located in {self.location}"

    def rent(self, num_days):
        self.is_rented = True
        self.rental_duration = num_days

class XUV(Car):
    category="XUV's"
    def __init__(self, company, model, location,number_of_passenger):
        super().__init__(company, model, location,number_of_passenger)
        total_passenger = number_of_passenger

# List Of the Cars 
car_list = [Car("Tesla", "Model S","ahmedabad"), Car("BMW", "3 Series", "ahmedabad"), Car("Toyota", "Camry","vadodra")]

class CarRental:
    def __init__(self, car_list):
        self.car_list = car_list

    def rent_car(self):
        location = input("Enter the rental location: ")
        company = input("Enter the company of the car you would like to rent: ")
        model = input("Enter the model of the car you would like to rent: ")
        num_days = int(input("Enter the number of days you would like to rent the car for: "))
        rental_purpose = input("Enter the purpose of rental (Personal/Business): ")
    #     insurance = input("Do you require insurance? (Yes/No): ")
        available_cars = [car for car in self.car_list if car.company == company and car.model == model and car.location == location]
        if not available_cars:
            return "Sorry, no cars of that company and model are available at this location."
        else:
            chosen_car = available_cars[0]
            chosen_car.rent(num_days)
            #rental_cost = rental_cost.calculate_cost(self,rental_purpose, insurance)
            return f"You have successfully rented a {company} {model} at {location} for {num_days} days with rent of ruppees."

    # def calculate_cost(self,rental_purpose,insurance):
    #     base_cost=chosen_car.rental_duration * 100
    #     if rental_purpose=="Business":
    #         base_cost+=base_cost + 100

    #     if insurance=="YES":
    #         base_cost+=base_cost + 50

    def add_car(self):
        company2 = input("Enter the company of the car you would like to add: ")
        model2 = input("Enter the model of the car you would like to add: ")
        location2 = input("Enter the location: ")
        new_Car=Car(company2,model2,location2)
        self.car_list.append(new_Car)
        print(f"{model2} car is added at {location2}")

    def remove_car(self):
        company3 = input("Enter the company of the car you would like to remove: ")
        model3 = input("Enter the model of the car you would like to remove: ")
        location3 = input("Enter the location: ")
        remove_Car=Car(company3,model3,location3)
        available_cars = [car for car in self.car_list if car.company == company3 and car.model == model3 and car.location == location3]
        if not available_cars:
            return "Sorry, no cars of that company and model are available at this location."
        else:
            self.car_list.remove(remove_Car)
            print(f"{model3} is removed.")
    
    def available_car(self):
        for car in self.car_list:
            print(car)

rental = CarRental(car_list)

def main():
    while True:
        location_choice = input("Enter location (AHMEDABAD or VADODRA in lower case): ")
        if location_choice.lower() not in ["ahmedabad", "vadodra"]:
            print("Location not available to us right now!")
            continue
        
        print("1. Rent Car")
        print("2. Add Car")
        print("3. Remove Cars")
        print("4. Available Cars")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print(rental.rent_car())
        elif choice == "2":
            print(rental.add_car())
        elif choice == "3":
            print(rental.remove_car())
        elif choice == "4":
            print(rental.available_car())
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

if __name__ == "__main__":
    main()