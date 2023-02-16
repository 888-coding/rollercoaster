# Rollercoaster app
# Made with PYTHON

print("Welcome to the Rollercoaster!")
age = int(input("Please enter your age: "))
height = float(input("How tall are you (cm) ? "))
price = 0 

#Conditions
## If less than 120 cm , you cant play
## If you are between 18 to 49 years old, you pay 10 more bucks 
## If you want photo, add 10 bucks.
## Ticket normal price is 15 

if height >= 120:
    price_initial = 15
    price = price_initial
    if age >= 18 and age <= 49:
        price += 10
    
    wantPhoto = str(input("Do you want photo (y/n)? ")).lower()
    if wantPhoto == "y":
        price += 10
    
    print(f"Your ticket is going to cost : {price}")    
else:
    print("You don't have height to play this.")
