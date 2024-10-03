# Temperature Calculator

unit = input("Enter Temperature unit Celsius or Fahrenheit (C/F) :")
temp = float(input("Enter the temprature : "))


if unit == "C" :
    temp = round((9 * temp ) / 5 + 32, 1)
    print(f"The Temperature in Fahrenheit is : {temp}°F")
elif unit == "F" : 
    temp = round((temp - 32 ) * 5 / 9, 1)
    print(f"The Temperature in Celsius is : {temp}°C")

else:
    print(f" '{unit}' is not measureable unit") 