def calculate_BMI(weight, height):
    return weight/(height**2)
def bmi_categorie(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
def main():
    print("====BMI Calculator====")
    weight = float(input("Enter your weight:"))
    height = float(input("Enter your height:"))
    bmi = calculate_BMI(weight,height)
    categorie = bmi_categorie(bmi)

    print(f"\nYour BMI is {bmi:.2f}")
    print(f"Categorie {categorie}")

if __name__ == "__main__":
    main()