print("Welcome to the weight converter calculator!")
print("This program converts weight from kilograms to pounds.")

def kg_to_pounds(weight_kg):
    conversion = 2.20462
    pounds = weight_kg * conversion
    return pounds

weight_kg = float(input("Enter your weight in kilograms: "))

weight_pounds = kg_to_pounds(weight_kg)
print(f"The converted weight in pounds is: {weight_pounds:.2f}")



