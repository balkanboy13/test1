#Personal information
print("Dino Bibic")
print("Verdilaan,68 7002LP Doetinchem")
print("123456789")
print("HAN")

#Sales Prediction
def cal_profit():
    total_sale = input("Enter your total sale: ")
    annual_profit = float(total_sale) * 0.23
    print(annual_profit)
#cal_profit()

#Total Purchase
def total_purchase():
    price = float(input("Enter your total sale: "))
    subtotal = price * 5
    sales_tax = subtotal * 0.07
    total = subtotal + sales_tax

    print(total)
#total_purchase()

#Distance Traveled
def distance_traveled():
    speed = 70
    time = int(input("time traveled: "))

    distance = speed * time

    print(distance)
#distance_traveled()

#Miles-perGallon
def cal_mpg():
    miles_driven = input("miles driven:")
    gallons_of_gas = input("gallons of gas:")

    mpg = float(miles_driven) / float(gallons_of_gas)

    print(mpg)
#cal_mpg()

#Ingredient Adjuster
def ingredient_adjust():
    ammount_of_cookies = int(input("ammount of cookies:"))
    cup_of_sugar = 1.5 * ammount_of_cookies
    cup_of_butter = 1 * ammount_of_cookies
    cups_of_flour = 2.75 * ammount_of_cookies

    adjust = cup_of_butter + cup_of_sugar + cups_of_flour
    print(adjust)
ingredient_adjust()


