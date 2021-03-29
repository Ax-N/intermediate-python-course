import random 
def main():
   diceRolls = 2
   diceSum = 0
   for i in range(0,diceRolls):
    roll = random.randint(1,6)
    diceSum += roll
    print(f'You rolled a {roll}')
  print(f'You have rolled a total of {diceSum}')

if __name__== "__main__":
  main()