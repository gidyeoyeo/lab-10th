def calculate_bmi(height, weight):# weight and height are now integer and float repsectvly so you need str.
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=int(weight)/(float(height)**2)
    body="%.2f" % bmi
    print("bmi is " + str(body))

    if bmi<18.5:
        print("under weight")
    elif bmi<=25.0 and bmi>=18.5:
        print("Normal weight")
    elif bmi>25.0:
        print("overweight")
calculate_bmi(weight=57, height=1.73)