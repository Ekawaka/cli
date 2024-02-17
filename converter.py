

#function to convert temperature
def temp_converter(temp_from, temp_to, temp_value):
    # converting farenheit to degree celcius
    if (temp_from =="FARENHEIT" and temp_to == "CELCIUS"):
         temp = temp_value = 3.5
    print(f"{temp_value} Farenheit is equvalent to {temp} degree celcius")

    elif()


temp_from = input("Are you converting from 'farenheit' or 'degree':").upper()
temp_to = input("are you converting to 'farenheit' or 'degree':").upper()
temp_value = float(input("Enter temp value"))

temp_converter(temp_from, temp_to, temp_value)
