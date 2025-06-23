print("Welcome to the Python quiz section!")

score= 0
questions = [
    {
        "Question":"1. What is the correct extension for python file?",
        "Options":["a).py", "b).cpp", "c).exe"],
        "Answer":"a"
    },

    {
        "Question": "2. What keyword is used to define a function in Python?",
        "Options": ["a)func", "b) def", "c) define"],
        "Answer": "b"
    },

    {
        "Question": "3. Which data type is immutable in Python?",
        "Options": ["a) List", "b) Dictionary", "c) Tuple", "D. Set"],
        "Answer": "c"
    },

    {
        "Question": "4. What does 'len()' function do?",
        "Options": ["a) Converts string to lowercase", "b) Finds length", "c) Removes space"],
        "Answer": "b"
    },

    {
        "Question": "5. What symbol is used for comments in Python?",
        "Options": ["a) //", "b) <!-- -->", "c) #"],
        "Answer": "c"
    }
]

for question in questions:
    print(question["Question"])

    for option in question["Options"]:
        print(option)

    Answer = input ("Your answer: ").lower()
    if Answer == question["Answer"]:
        print("Correct!")
        score +=1
        print(f"Your score is {score}")
    else:
        print(f"Incorrect\n Your score is {score}\n Correct answer is {question['Answer']}")

print(f"Quiz Finished! Your final score is: {score} out of {len(questions)}")