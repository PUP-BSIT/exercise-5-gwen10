
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

print("\n(Gerald Sario) What is the square of 12?")
print("a) 124 		             c) 144")
print("b) 132   	             d) 155")

your_answer5 = input("Enter your answer: ") 

if your_answer5 == 'c' or your_answer5 == 'C':
    print ("Your answer is correct!")
    total_score += 1 
else:
    print(f"{your_answer5} is incorrect. The correct answer is C.")

print("\n(Gwen Teves) Who was the first president of the Philippines?")
print("a) Manuel L. Quezon       c) Jose P. Laurel")
print("b) Emilio Aguinaldo       d) Ferdinand Marcos")

your_answer6 = input("Enter your answer: ")

if your_answer6 == "b" or your_answer6 == "B":
    print("Your answer is correct!")
    total_score += 1
else:
    print(f"{your_answer6} is incorrect. The correct answer is B.")

print("\n(Alexa Gonato) Which planet is known as the Red Planet?")
print("a) Venus                  c) Mars")
print("b) Jupiter                d) Saturn")

your_answer7 = input("Enter your answer: ")

if your_answer7 == "c" or your_answer7 == "C":
    print("Your answer is correct!")
    total_score += 1
else:
    print(f"{your_answer7} is incorrect. The correct answer is C.")

print("\n(Christian Bataller) Guess my favorite quote?")
print("a) 'Dream big, work hard.'")           
print("b) 'Happiness depends on ourselves.'")
print("c) 'What is meant for you will always find its way.'")
print("d) 'Everything happens for a reason.'")

your_answer8 = input("Enter your answer: ")

if your_answer8 == "c" or your_answer8 == "C":
    print("Your answer is correct!")
    total_score += 1
else:
    print(f"{your_answer8} is incorrect. The correct answer is C.")

print("\n(Kian Miguel) He was known the greatest scorer of all time in NBA?")
print("a) Michael Jordan          c) Stephen Curry")
print("b) Kobe bryant             d) Lebron James")

your_answer9 = input("Enter your answer: ")

if your_answer9 == "d" or your_answer9 == "D":
    print("Your answer is correct!")
    total_score += 1
else:
    print(f"{your_answer9} is incorrect. The correct answer is D.")

print("\n(Gerald Sario) What is the 5th term of the arithmetic sequence:")
print("2,5,8,11,..?")
print("a) 14 		              c) 15")
print("b) 12                      d) 16")

your_answer10 = input("Enter your answer: ")

if your_answer10 == 'a' or your_answer10 == 'A':
    print("Your answer is correct!")
    total_score += 1
else:
    print(f"{your_answer10} is incorrect. The correct answer is A.")
    
print(f"\nCongratulations! You got {total_score} out of 10 items.")
print("Thank you for answering!")