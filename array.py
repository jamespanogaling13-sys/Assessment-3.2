# ASSESSMENT 3.2 - ARRAY
# Name: JAMES PANOGALING

def main():
    name = "JAMES PANOGALING".replace(" ", "")

    array = []

    print("=== ARRAY INSERTION ===")

    for letter in name:
        array.append(letter)

    print("Array:", " -> ".join(array))

    print("\n=== ARRAY DELETION ===")

    while len(array) > 0:
        removed = array.pop(0)
        print("Removed:", removed)
        print("Remaining:", array)

    print("\nFinal Array: EMPTY")


main()