"""Certificate Eligibility"""

all_days = input("do you have attendence for all 5 days ?")

if all_days == "yes":
    assignment = input("Have you completed assignments for each day before deadline?")
    if assignment == "yes":
        liveclass = input("Have you attended the classes live and not recorded?")
        if liveclass == "yes":
            camera = input("Was your camera on for entire duration of class?")
            print("Congratulations! You are eligible for the certificate :)")
else:
    print("sorry! you are not eligible for the certificate")