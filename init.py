import json, sys, random
f = sys.argv[1]
data = json.load(open(f))

while True:
    question = random.choice(list(data.items()))
    answer = input(f"{question[0]}: ")
    if answer == question[1]:
        print("Answer is correct")
    else:
        print("Answer is incorrect")
        print(f"Correct answer: {question[1]}")
