
pointsPossible = 100
#type student's name below after the input (in the "" :"")
#scroll down to the bottom for typing in the numeric grade
studentname = input("Teddy:")


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
    #type the numeric score the student recieved below(after input in the " ")
    score = int(input("100:"))
    calcthegrade()
except Exception:
    print("Please provide valid number")





