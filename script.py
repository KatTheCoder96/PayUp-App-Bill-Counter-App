# float() converts decimal numbers so you can calculate money easily 
# int() converts whole numbers 
# input() function always reads data as a string even if you type a number which is not correct . it is a typerror
# must convert input stringgs into numbers either intergers or floats when doing math 
# cmd / to comment and uncomment code
print("Welcome to PayUp!")

event = input("What was the event? ")
cost = float(input("How much was the cost? "))
service_charge = int(input("Was there a tip or a service charge? Enter a whole number (e.g. 20 for 20%): ").strip("%"))

group_size = int(input("How many people were in your group? "))
service_charge_total = cost * service_charge / 100
grand_total = cost + service_charge
total_per_person = grand_total / group_size

print() 
print(f"Here's the breakdown for {event}:")
print()
print(f"Cost: ${cost:.2f}")
print(f"Service charges: ${service_charge_total:.2f}")
print(f"Group size: {group_size}")
print(f"Grand total: ${grand_total:.2f}")
print()
print(f"Each person must PayUp: ${total_per_person:.2f}")


