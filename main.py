
total_score = 0

print("\nWelcome to GWN10's team quiz!")
print("You will be asked 10 questions. Please answer them correctly.")

print("\n(Gwen Teves) Who is known as the Father of the Philippine Revolution?")
print("a) Jose Rizal             c) Andres Bonifacio")
print("b) Emilio Aguinaldo       d) Antonio Luna")

your_answer1 = input("Enter your answer: ")

if your_answer1 == "c" or your_answer1 == "C":
    print("Your answer is correct!")
    total_score += 1
else:
    print(f"{your_answer1} is incorrect. The correct answer is C.")