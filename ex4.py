# number of cars available
cars  = 100
# number of people each car holds
space_in_a_car = 4
# quantity of drivers that are available
drivers = 30
# quantity of passengers needing transport
passengers = 90
# cars that will be available once everyone is transported
cars_not_driven = cars - drivers
# how many cars will be used
cars_driven = drivers
# the total capacity of all vehicles based on # of drivers
carpool_capacity = cars_driven * space_in_a_car
# dividing passengers by car drivers provides how many passengers in each vehicle on average
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "there will be",cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We need to put about", average_passengers_per_car, "in each car."