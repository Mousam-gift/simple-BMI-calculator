weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meter:"))

bmi = weight/(height**2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 24.9:
    category = "normal weight"
elif bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"
    
print("your BMI is:",round(bmi,2))
print("category:",category)