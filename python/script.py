import random

def main():
    print("Welcome to rock paper scissors! \n1. Play \n2. Quit")
    playerMove = int(input("Enter: "))
    if playerMove == 1:
        playActive = True
    if playerMove == 2:
        return
    

    playerPoints = 0
    cpuPoints = 0

    while playActive == True:
        
        print("1. Rock \n2. Paper \n3. Scissors \n4. Quit")
        playerInput = int(input("Enter your move: "))
        if playerInput == 1:
            print("You chose rock.")
        elif playerInput == 2:
            print("You chose paper.")
        elif playerInput == 3:
            print("You chose scissors.")
        elif playerInput == 4:
            playActive = False
        else:
            print("Invalid input. Please try again.")
            continue

        cpuMove = random.randint(1, 3)

        if cpuMove == 1:
            print("CPU chose rock.")
        elif cpuMove == 2:
            print("CPU chose paper.")
        else:
            print("CPU chose scissors.")

        if playerInput == 1 and cpuMove == 1:
            print("It's a tie! No points awarded.")
        elif playerInput == 1 and cpuMove == 2:
            print("CPU wins and gets the point.")
            cpuPoints += 1
        elif playerInput == 1 and cpuMove == 3:
            print("You win and get the point.")
            playerPoints += 1
        elif playerInput == 2 and cpuMove == 1:
            print("You win and get the point.")
            playerPoints += 1
        elif playerInput == 2 and cpuMove == 2:
            print("It's a tie! No points awarded.")
        elif playerInput == 2 and cpuMove == 3:
            print("CPU wins and gets the point.")
            cpuPoints += 1
        elif playerInput == 3 and cpuMove == 1:
            print("CPU wins and gets the point.")
            cpuPoints += 1
        elif playerInput == 3 and cpuMove == 2:
            print("You win and get the point.")
            playerPoints += 1
        elif playerInput == 3 and cpuMove == 3:
            print("It's a tie! No points awarded.")

        print("Player points: " + str(playerPoints))
        print("CPU points: " + str(cpuPoints))
        print("\n")
main()