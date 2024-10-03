# Python weight Calculator

weight = float(input("Enter your Weight: "))
unit = input( "Kilograms or Pounds? (K or L): ")


if unit == "K" :
    weight = weight * 2.205
    unit = "Lbs."

    print(f"Your Weight is : {round(weight , 1)} {unit}")


elif unit == "L" :
    weight = weight / 2.205
    unit = "Kgs."

    print(f"Your Weight is : {round(weight , 1)} {unit}")

else :
    print(f"{unit} was not valid")


    # print(f"Your Weight is : {round(weight , 1)} {unit}")
