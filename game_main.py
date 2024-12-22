import difflib
import random

with open("words.txt", 'r', encoding='utf-8') as file:
    words = [line.strip() for line in file.readlines()]


def reload():
    return start(words) if input("Anther game?:(y/n)").strip().lower() == "y" else exit(0)


def start(words):
    chosen_word = random.choice(words)
    num = 10
    correct = list(chosen_word)
    length = len(chosen_word)
    print(f"The length of this word: {length}")
    output = ""
    while num:
        inputed = input("guess word:").lower()
        if inputed == chosen_word:
            print(f'\033[92myou won, the correct word is "{chosen_word}"\033[0m')
            reload()
        if inputed not in words:
            close_matches = difflib.get_close_matches(inputed, words, 1, 0.6)
            print(f'inputed error (\033[31m"{inputed}"\033[0m)', end="")
            if close_matches:
                print(f', Did you mean "{close_matches[0]}"?')
            else:
                print()
            continue
        list_inputed = [i for i in inputed]
        for _ in range(len(correct) - len(list_inputed)):
            list_inputed.append("_")
        for i in range(length):
            if list_inputed[i] == correct[i]:
                output += f"\033[92m{list_inputed[i]}\033[0m "
            elif list_inputed[i] in correct:
                output += f"\033[93m{list_inputed[i]}\033[0m "
            else:
                output += f"\033[90m{list_inputed[i]}\033[0m "
        print(output)
        remaining_letters = [chr(i) for i in range(97, 123) if chr(i) not in inputed]
        print(f"haven't tried: {''.join(remaining_letters)}", end="")
        num -= 1
        output += "\n"
        print(f"        {num}chance left") if num == 1 else print(f"        {num} chances left")
    print(f'\033[31myou lose, the correct word is "{chosen_word}"\033[0m')
    reload()


if __name__ == "__main__":
    start(words)
