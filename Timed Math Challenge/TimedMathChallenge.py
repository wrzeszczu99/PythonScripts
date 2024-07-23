import random;
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 2
MAX_OPERAND = 13
TOTAL_EQUATIONS = 5

def generate_equation():
    operator = random.choice(OPERATORS)
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)

    equation = str(left) + operator + str(right)
    answer = eval(equation)
    return equation, answer


wrong_guesses = 0
input(str(TOTAL_EQUATIONS) + " math problems before you! Press Enter to start")

start_time = time.time()

for i in range(TOTAL_EQUATIONS):
    equation, answer = generate_equation()
    while True:
        guess = input(equation + " = ")
        if(guess == str(answer)):
            break
        wrong_guesses +=1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("Great Work! You solved "+str(TOTAL_EQUATIONS) +" problems in: "+str(total_time)
      +" seconds! You was wrong only: "  + str(wrong_guesses) + " times.")   
      