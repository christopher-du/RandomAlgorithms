from SkipList import SkipList
import random

def cmd():
    while True:
        skippy = SkipList(14)
        for x in range(6000):
            skippy.insert(random.randint(1, 4098))
        skippy.print()
        point = skippy.head
        breaker = 0;
        while True:
            userInput = input("Command: ")
            if (userInput == "n"):
                point = point.next
                skippy.print()
                print(point)
            elif (userInput == "d"):
                point = point.down
                skippy.print()
                print(point)
            elif (userInput == "s"):
                searchNum = input("Key: ")
                print("UserInput: ", searchNum)
                skippy.search(int(searchNum))
            else:
                breaker = userInput
                break
        if breaker == "b":
            break


def main():
    return 0


main()
