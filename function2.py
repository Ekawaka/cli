#fx helps to modularise our codes.
#def square():
#def quality_assurance():
    #return 5**2

#print(square())

#parameters
#arguments 
#def square(num):
    #return num**2

#print(square(76))

#num = int(input("Enter the value:"))
#print(f" The square of{num} is{square(num)},")


# write a function that calculates the total phone bill in a month

#def phone_bill(num):
    #return num*30
#num = int(input("Enter the value:"))
#print(f"The phone_bill{num} is {num*30},")

def my_phone_bill(dailybill, days_in_a_month):
    monthly_bill = dailybill * days_in_a_month
    return monthly_bill

dailybill = float(input("Enter your daily phone bill: "))
days = int(input("How many days in a month?"))

print (my_phone_bill(dailybill, days))





    