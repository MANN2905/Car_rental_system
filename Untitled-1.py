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

car_list = [Car("Tesla", "Model S","ahmedabad"), Car("BMW", "3 Series", "ahmedabad"), Car("Toyota", "Camry","vadodra")]

class CarRental:
    def __init__(self, car_list):
        self.car_list = car_list

    def rent_car(self):
        location = input("Enter the rental location: ")
        company = input("Enter the company of the car you would like to rent: ")
        model = input("Enter the model of the car you would like to rent: ")
        num_days = int(input("Enter the number of days you would like to rent the car for: "))
        #rental_purpose = input("Enter the purpose of rental (Personal/Business): ")
        #insurance = input("Do you require insurance? (Yes/No): ")
        
        available_cars = [car for car in self.car_list if car.company == company and car.model == model and car.location == location]
        if not available_cars:
            return "Sorry, no cars of that company and model are available at this location."
        else:
            chosen_car = available_cars[0]
            chosen_car.rent(num_days)
            #rental_cost = chosen_car.calculate_cost(rental_purpose, insurance)
            return f"You have successfully rented a {company} {model} at {location} for {num_days} days."
    # def calculate_cost(self, rental_purpose, insurance):
    #     base_cost = num_days * chosen_car.daily_rate
    #     if rental_purpose == "Business":
    #         base_cost += base_cost * 0.1
        
    #     if insurance == "Yes":
    #         base_cost += base_cost * 0.2
            
    #     return base_cost
    def add_car(self):
        company2 = input("Enter the company of the car you would like to add: ")
        model2 = input("Enter the model of the car you would like to add: ")
        location2 = input("Enter the location: ")
        new_Car=Car(company2,model2,location2)
        self.car_list.append(new_Car)
        return car_list
            
# Example usage

rental = CarRental(car_list)
rental.add_car()
for car in car_list:
    print(car)
