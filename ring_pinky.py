#!/usr/bin/env python

import time
import random

from rich.progress import track

# Finger exercise: Finger taps
def finger_taps(finger_name):
    print(f"Tap your {finger_name} finger on a flat surface rapidly for 30 seconds.")
    time.sleep(30)
    print("Great! Let's move on to the next exercise.")

# Finger exercise: Finger stretches
def finger_stretches(finger_name):
    print(f"Extend and stretch your {finger_name} finger as far as you can for 10 seconds.")
    time.sleep(10)
    print("Relax and repeat the stretch for 5 times.")

# Typing practice: Random word generator
def typing_practice():
    words = ['pearl', 'keyboard', 'jazz', 'blanket', 'guitar', 'ring', 'pinky', 'exercise', 'fingers']
    print("Let's practice typing with your ring and pinky fingers!")
    print("Type the word you see and press Enter. Ready? Go!")
    i = 0
    tot = 10
    for i in range(tot):
        word = random.choice(words)
        print(word)
        user_input = input()
        if user_input.lower() == word:
            print("Correct!")
        else:
            print("Incorrect. Try again.")
        i += 1
        print(f"{i}/{tot} (Ctrl+C to quit)")

# Main program
print("Welcome to the Finger Strength and Typing Practice Program!")

while True:
    print("\nMenu:")
    print("1. Finger Taps Exercise")
    print("2. Finger Stretches Exercise")
    print("3. Typing Practice")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        finger_taps("ring and pinky")
    elif choice == '2':
        finger_stretches("ring and pinky")
    elif choice == '3':
        typing_practice()
    elif choice == '4':
        print("Thank you for using the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
