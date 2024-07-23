import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

SYMBOLS = {
    "@" : 2,
    "7" : 4,
    "*" : 6,
    "☺" : 8
}
SYMBOLS_MULTIPLIER = {
    "@" : 5,
    "7" : 4,
    "*" : 3,
    "☺" : 2
}

def check_rows(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)

    return winnings, winning_lines

def spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_value in symbols.items():
        for _ in range(symbol_value):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns)):
        for i, col in enumerate(columns):
            if i != len(columns) -1:
                print(col[row], end=" | ")
            else:
                print(col[row])

def deposit():
    while True:
        amount = input("How many would you like to deposit($)? ")
        if(amount.isdigit()):
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Must be positive integer.")
        else:
            print("Must be a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on(1-" +str(MAX_LINES)+")? ")
        if(lines.isdigit()):
            lines = int(lines)
            if 1<= lines <=MAX_LINES:
                break
            else:
              print("Must be between 1 and " +str(MAX_LINES)+"(inclusive).")
        else:
            print("Must be a number.")
    return lines

def get_bet(balance, lines):
    while True:
        amount = input("What would you like to bet on each line($)? ")
        if(amount.isdigit()):
            amount = int(amount)
            if MIN_BET<= amount <=MAX_BET and amount * lines <= balance:
                break
            else:
                print(f"Must be between ${MIN_BET} - ${MAX_BET}. And your balance is: ${balance}(you tried to bet: ${amount*lines})")
        else:
            print("Must be a number.")
    return amount

def gameloop(balance):
    lines = get_number_of_lines()
    bet = get_bet(balance,lines)
    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${bet*lines}")
    slots = spin(ROWS, COLS, SYMBOLS)
    print_slot_machine(slots)
    winnings, winning_lines = check_rows(slots, lines, bet, SYMBOLS_MULTIPLIER)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)
    return winnings - bet*lines

def main():
    balance = deposit()
    while True:
        print(f"Currens balance is ${balance}")
        spin = input("Press enter to play, or write q to quit ")
        if spin.lower() == "q":
            break
        balance += gameloop(balance)
    
    print(f"You left with ${balance}")

main()