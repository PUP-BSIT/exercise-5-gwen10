
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

print("\n(Alexa Gonato) Which of the following is the capital of Canada?")
print("a) Toronto               c) Ottawa")
print("b) Vancouver             d) Montreal")

your_answer2 = input("Enter your answer: ")

if your_answer2 == "c" or your_answer2 == "C":
    print("Your answer is correct!")
    total_score += 1
else:
    print(f"{your_answer2} is incorrect. The correct answer is C.") 

print("\n(Christian Bataller) Which activity do I enjoy when bored?")
print("a) Cooking               c) Painting")
print("b) Singing               d) Basketball") 

your_answer3 = input("Enter your answer: ")

if your_answer3 == "b" or your_answer3 == "B":
    print("Your answer is correct!")
    total_score += 1
else:
    print(f"{your_answer3} is incorrect. The correct answer is B.")

print("\n(Kian Miguel) Who is the young MVP in NBA?")
print("a) Lebron James           c) Kevin Durant")
print("b) Derick Rose            d) Kyrie Irving")

your_answer4 = input("Enter your answer: ")

if your_answer4 == "b" or your_answer4 == "B":
    print("Your answer is correct!")
    total_score += 1
else:
    print(f"{your_answer4} is incorrect. The correct answer is B.")
