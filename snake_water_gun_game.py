# Snake, Water, Gun game 

import random
computer = random.choice(['water', 'Gun', 'Snake'])
me = input("Enter my choice: ")

if computer == 'water' and me == 'Gun': 
    print("You Lose")
elif computer == 'Snake' and me == 'water':
    print("You Lose")
elif computer == 'Gun' and me == 'Snake': 
    print("You Lose")
elif computer == 'Gun' and me == 'water': 
    print("You win")
elif computer == 'water' and me == 'Snake': 
    print("You win")
elif computer == 'Snake' and me == 'Gun': 
    print("You win")
else: 
    print("Draw!")

print("Computer chose:", computer)
print("You chose:", me)