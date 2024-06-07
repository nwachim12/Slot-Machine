import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 1000

ROWS = 3
COLUMNS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C" : 2,
    "D": 1
}
def check_wins(cols, lines, bet,value):
    amount = 0
    lines_win = []
    for line in range(lines):
        symbol = cols[0][line]
        for column in cols:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            amount += value[symbol] * bet
            lines_win.append(line +1)
    return amount, lines_win

def machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1 :
                 print(column[row], end = " | ")
            else:
                print(column[row], end = "")
        print()
def deposit():
    while True:
        amount = input("Deposit Amount $:")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("This is less than 0")
        else:
            print("Enter valid number")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Line Amount (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines and lines <= MAX_LINES:
                break
            else:
                print("This is less than 0")
        else:
            print("Enter valid number")

    return lines

def betting():
    while True:
        amount = input("Bet Amount for each Line $:")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"This must between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Enter valid number")

    return amount

def game_loop(balance):
    lines = get_number_of_lines()
    while True:
        bet = betting()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Not enough amount to bet, current balance is ${balance}")
        else:
            break

    print(f"Betting ${bet} on {lines} lines. Total equals to ${total_bet}")
    slots = machine_spin(ROWS, COLUMNS, symbol_count)
    print_machine(slots)
    win, lines_win = check_wins(slots, lines, bet, symbol_value)
    print(f"You won ${win}")
    print(f"Won on lines: ", *lines_win)
    return win - total_bet
def main():
    balance = deposit()
    while True:
        print(f"Balance is ${balance}")
        answer = input("Press enter to spin or Q to quit")
        if answer.lower() == "q":
            break
        balance += game_loop(balance)
    print(f"Final balance: ${balance}")

main()