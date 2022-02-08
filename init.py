import json, sys, random
f = sys.argv[1]
data = json.load(open(f))

while True:
    question = random.choice(list(data.items()))
    answer = input(f"{question[0]}: ")
    print(f"Answer is: {'correct' if answer == question[1] else 'incorrect'}")
    print(f"Correct answer: {question[1]}")
