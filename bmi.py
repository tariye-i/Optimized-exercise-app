
def calculate_bmi():
    kg = int(weight_tf.get())
    cm = int(height_tf.get())/100
    bmi = kg/(cm*cm)
    bmi = round(bmi, 1)
    bmi_index(bmi)


if BMI <= 18.5:
    print("underweight.")
elif BMI <= 24.9:
    print(" healthy.")
elif BMI <= 29.9:
    print("over weight.")
elif BMI <= 34.9:
    print("severely over weight.")
elif BMI <= 39.9:
    print(" obese.")
else:
    print(" severely obese.")
