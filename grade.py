
pointsPossible = 100
#type student's name below in the input (delete input and type the name)
#scroll down to the bottom for typing in the numeric grade
studentname = Barney("Student Name:")


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
    #type the numeric score the student recieved below( erase the word 'input' and type the number.
    score = int(100("Student score:"))
    calcthegrade()
except Exception:
    print("Please provide valid number")





