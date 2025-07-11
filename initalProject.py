#student grade check
#Accept the input from the user for Name and Roll Number,
#Define Three subjects for the percentage calculation
#IF percentage is >80 then 1st division
#else percentage is >-60 and <80 then 2nd division

def grade_check():
    #Firstly take the input as Name from user;
    name = input("Please Enter your Name:")

    roll_Number = input("Please ENter your Roll Number:")

    student_detail = (name, roll_Number)


    subjects = ["Math", "Science", "Computer"]

    d = {}

    for subject in subjects:
        marks = input (f"Enter your marks in {subjects}:")
        d[subject] = marks
    
    value = sum(d.values())
    totalPercentage = value / len(subjects)

    print(f"This is the total percentage: {totalPercentage}")

    print(f"This is the Value of dictionary (d)")


    if totalPercentage > 80:
        print("1st Division")
    else:
        print("2nd Division")
 