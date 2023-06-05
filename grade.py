
pointsPossible = 100

studentname = input("Student Name:")
def calcthegrade():
    if 100 >= score >= 90:
        grade = "A"
    elif 90 > score >= 80:
        grade = "B"
    elif 80 > score >= 70:
        grade = "C"
    elif 70 > score >= 60:
        grade = "D"
    else :
        grade = "F"
    print("{} - {}".format(studentname, grade))

try:
    score = int(input("Student score:"))
    calcthegrade()
except Exception:
    print("Please provide valid number")





