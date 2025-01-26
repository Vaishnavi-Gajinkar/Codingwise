level = input("Are you a fresher or experienced student? ")
course_name = ""

if (level == "fresher") or ("Fresher") or ("FRESHER"):
    course_name = input(""" Enter your course you would like to pursue.
                            1. web Dev
                            2. App Dev
                            3. DS / ML / AI
                        """)
    if course_name == "web dev":
        print("Learn HTML, Css, Js, Python Django")
    elif course_name == "app dev":
        print("Learn Java + Dsa + Build Projects")
    elif course_name == "ds, ml, ai":
        print("Learn Python, Maths, R")
    else:
        print("Invalid Input")

elif (level == "experienced") or (level == "Experienced") or (level == "EXPERIENCED"):
    course_name = input(""" Enter your course you would like to pursue.
                            1. Data Analytics
                            2. Cloud Computing
                            3. Front-End
                        """)
    if course_name == "Data Analytics":
        print("Learn Python, Excel, PowerBI")
    elif course_name == "Cloud Computing":
        print("Learn DevOps & Python for Automation")
    elif course_name == "Front-End":
        print("Learn Python and Django for Backend")
    else:
        print("Invalid Input")