""" Grade Calculator """

subj1 = float(input("Enter marks of subject 1"))
subj2 = float(input("Enter marks of subject 2"))
subj3 = float(input("Enter marks of subject 3"))

avg = (subj1 + subj2 + subj3) / 3

if avg >= 90:
    print("Grade A")
elif avg >= 80 and avg < 90:
    print("Grade B")
elif avg >= 70 and avg < 80:
    print("Grade C")
else:
    print("Grade D")