# ASSESSMENT 3.2 - STACK
# Name: JAMES PANOGALING

def main():
    name = "JAMES PANOGALING".replace(" ", "")

    stack = []

    print("=== STACK INSERTION (PUSH) ===")

    for letter in name:
        stack.append(letter)

    print("Stack:", stack)

    print("\nStack (TOP TO BOTTOM):")

    for letter in reversed(stack):
        print(letter)

    print("\n=== STACK DELETION (POP) ===")

    while len(stack) > 0:
        removed = stack.pop()
        print("Popped:", removed)
        print("Remaining:", list(reversed(stack)))

    print("\nFinal Stack: EMPTY")


main()