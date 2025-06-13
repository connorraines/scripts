MetricOrImperial = input("Do you want to use Metric or Imperial units? (M/I): ").strip().upper()

if MetricOrImperial == "M":
    bodyWeight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    bmi = bodyWeight / (height ** 2)
    print("Your BMI is: ", bmi)
elif MetricOrImperial == "I":
    bodyWeight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    bmi = (bodyWeight / (height ** 2)) * 703
    print("Your BMI is: ", bmi)
else:
    print("Invalid input. Please enter 'M' for Metric or 'I' for Imperial.")