
print("Welcome to Python Student Report Card!")
name = input("What is your name? ")
obtain_marks=list(map(int,input("How many marks do you have? ").split()))
print(f"Obtain marks of the student is {sum(obtain_marks)}")

Student_report={
        "Name":name,
        "Subject":["Mathematics", "Computer Science","English","Physics"],
        "Total_Marks": [100,100,100,100],
        "Obtain_marks":obtain_marks
}

cal_total_marks=sum(Student_report["Total_Marks"])
cal_obtain_marks=sum(Student_report["Obtain_marks"])
percentage_of_student=(cal_obtain_marks/cal_total_marks) *100
print(f"The percentage of student is {percentage_of_student}%")

if percentage_of_student >= 30:
    print("Congeatulations! You Pass.")
else:
    print("You fail the exam because your percentage is less than 30%")
