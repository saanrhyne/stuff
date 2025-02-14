# Imports and setting up variables
import random
import time
deck = ["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠",
        "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣",
        "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦",
        "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥"]

playerCards = []
hitStandPlayer = "H"
playerCardSum = 0

dealerCards = []
hitStandDealer = "H"
dealerCardSum = 0



# Function to draw cards
def draw(drawFromDeck, addToDeck, numberOfCards):
  random.shuffle(drawFromDeck)
  
  for i in range(numberOfCards):
    addToDeck.append(drawFromDeck[0])
    drawFromDeck.pop(0)



# Function to calculate and print the value of a set of cards
def cardValue(cards, whoseCards):
  sum = 0
  numAce = 0
  toPrint = ""
  
  for i in cards:
    if "A" in i:
      sum += 1
      numAce += 1
    elif "K" in i or "Q" in i or "J" in i or "1" in i:
      sum += 10
    else:
      sum += int(i[0])
    if "♥" in i or "♦" in i:
      toPrint += "\033[0;31m" + i + "\033[0m " # Adds red color to the card
    else:
      toPrint += i + " "
  
  for i in range(numAce): # Checks if the value of an Ace should be 1 or 11
    if sum + 10 <= 21:
      sum += 10

  print(toPrint)
  print("Sum of " + whoseCards + " cards: " + str(sum) + "\n")
  return sum



# Starting game
time.sleep(0.25)
print("\033[0;32m\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m")
time.sleep(0.25)
print("             Welcome to Blackjack")
time.sleep(0.25)
print("\033[0;32m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\033[0m") 
time.sleep(0.25)

draw(deck, playerCards, 2)
playerCardSum = cardValue(playerCards, "your")

draw(deck, dealerCards, 2)
dealerCardSum = cardValue(dealerCards, "dealer's")



# Player gameplay loop
time.sleep(0.25)
print("\033[0;32m\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m")
time.sleep(0.25)
print("                 Your Turn")
time.sleep(0.25)
print("\033[0;32m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\033[0m")
time.sleep(0.25)

while hitStandPlayer == "H" and playerCardSum <= 21: # Gameplay loop
  hitStandPlayer = input("[H]it or [S]tand").upper()

  while hitStandPlayer != "H" and hitStandPlayer != "S": # Checks for valid input
    hitStandPlayer = input("[H]it or [S]tand").upper()

  if hitStandPlayer == "H": # If hit is selected, draws a card and calculates new value
    draw(deck, playerCards, 1)
    playerCardSum = cardValue(playerCards, "your")

    if playerCardSum > 21: # Checks for break
      print("Break! You lose.")
      hitStandPlayer = "S"



# Dealer gameplay loop
time.sleep(0.25)
print("\033[0;32m\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m")
time.sleep(0.25)
print("               Dealer's Turn")
time.sleep(0.25)
print("\033[0;32m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\033[0m")
time.sleep(0.25)

while hitStandDealer == "H" and dealerCardSum <= 21: # Gameplay loop
  print("Dealer is thinking...")
  time.sleep(3)

  if (dealerCardSum <= 16 or dealerCardSum < playerCardSum) and playerCardSum <= 21: # Dealer hits
    print("Dealer chooses to hit")
    draw(deck, dealerCards, 1)
    dealerCardSum = cardValue(dealerCards, "dealer's")

  elif dealerCardSum <= 21: # Dealer stands if less than or equal to 21
    hitStandDealer = "S"
    print("Dealer chooses to stand")

  else: # If none of the above conditions are met, the dealer breaks
    print("Break! The dealer loses.")



# End result
time.sleep(0.25)
print("\033[0;32m\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m")
time.sleep(0.25)
print("                 Game Over")
time.sleep(0.25)
print("\033[0;32m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\033[0m")
time.sleep(0.25)

if playerCardSum == dealerCardSum: # A tie is always a tie
  print("You tied the dealer.")

elif dealerCardSum > 21 or (playerCardSum <= 21 and playerCardSum > dealerCardSum): # If the dealer breaks or the player beats the dealer
  print("You win!")

else: # If none of the above conditions are met, the player loses
  print("Ouch. You lose")
