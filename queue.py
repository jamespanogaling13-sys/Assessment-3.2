# ASSESSMENT 3.2 - QUEUE
# Name: JAMES PANOGALING

from collections import deque

def main():
    name = "JAMES PANOGALING".replace(" ", "")

    queue = deque()

    print("=== QUEUE INSERTION (ENQUEUE) ===")

    for letter in name:
        queue.append(letter)

    print("Queue:", list(queue))

    print("\n=== QUEUE DELETION (DEQUEUE) ===")

    while len(queue) > 0:
        removed = queue.popleft()
        print("Dequeued:", removed)
        print("Remaining:", list(queue))

    print("\nFinal Queue: EMPTY")


main()