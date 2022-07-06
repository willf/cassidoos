## Create a Chuck-a-Luck game class
import random

class ChuckALuck():
  def __init__(self, starting_balance = 500):
    self.balance = starting_balance
    self.turns = 0
    self.last_roll = None
    self.last_matches = None
    self.last_bet = None
    self.last_win = None
    self.last_loss = None

  def roll_dice(self):
    return random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)

  def play(self, chosen_number, bet):
    self.turns += 1
    self.last_bet = bet
    self.last_roll = self.roll_dice()
    self.last_matches = sum(1 for die in self.last_roll if die == chosen_number)

  def update_balance(self):
    self.last_loss = None
    self.last_win = None
    if self.last_matches == 0:
      self.last_loss = self.last_bet
      self.balance -= self.last_bet
    else:
      self.last_win = self.last_bet * self.last_matches
      self.balance += self.last_win
  
  def validate_bet(self, bet):
    if bet > self.balance:
      raise ValueError("You don't have enough money to bet that much!")
    if bet < 0:
      raise ValueError("You can't bet a negative amount!")

  def validate_number(self, number):
    if number < 1 or number > 6:
      raise ValueError("Number must be between 1 and 6!")

  def play_game(self):
    while self.balance > 0:
      print("Your balance is: {}".format(self.balance))
      if self.last_roll:
        print("Your last roll was: {}".format(self.last_roll))
      if self.last_matches:
        print("You matched {} dice!".format(self.last_matches))
      if self.last_win:
        print("You won {}!".format(self.last_win))
      if self.last_loss:
        print("You lost {}!".format(self.last_loss))
      print("What do you want to bet?")
      bet = int(input())
      print("Choose a number between 1 and 6:")
      chosen_number = int(input())
      self.validate_bet(bet)
      self.validate_number(chosen_number)
      self.play(chosen_number, bet)
      self.update_balance()
    return self.balance

if __name__ == "__main__":
  game = ChuckALuck()
  game.play_game()
  print("Your balance is: {}".format(game.balance))
  if game.last_roll:
    print("Your last roll was: {}".format(game.last_roll))
  if game.last_matches:
    print("You matched {} dice!".format(game.last_matches))
  print("You're out of money! Thanks for playing!")
  print("You played {} turns!".format(game.turns))


""" Example game output:

Your balance is: 500
What do you want to bet?
250
Choose a number between 1 and 6:
3
Your balance is: 250
Your last roll was: (6, 4, 2)
You lost 250!
What do you want to bet?
125
Choose a number between 1 and 6:
3
Your balance is: 375
Your last roll was: (3, 4, 5)
You matched 1 dice!
You won 125!
What do you want to bet?
200
Choose a number between 1 and 6:
3
Your balance is: 175
Your last roll was: (6, 2, 6)
You lost 200!
What do you want to bet?
100
Choose a number between 1 and 6:
2
Your balance is: 275
Your last roll was: (6, 1, 2)
You matched 1 dice!
You won 100!
What do you want to bet?
150
Choose a number between 1 and 6:
2
Your balance is: 125
Your last roll was: (1, 4, 6)
You lost 150!
What do you want to bet?
65
Choose a number between 1 and 6:
3
Your balance is: 60
Your last roll was: (1, 4, 4)
You lost 65!
What do you want to bet?
30
Choose a number between 1 and 6:
2
Your balance is: 90
Your last roll was: (5, 2, 1)
You matched 1 dice!
You won 30!
What do you want to bet?
45
Choose a number between 1 and 6:
2
Your balance is: 45
Your last roll was: (5, 5, 5)
You lost 45!
What do you want to bet?
25
Choose a number between 1 and 6:
2
Your balance is: 20
Your last roll was: (6, 3, 1)
You lost 25!
What do you want to bet?
10
Choose a number between 1 and 6:
2
Your balance is: 30
Your last roll was: (1, 4, 2)
You matched 1 dice!
You won 10!
What do you want to bet?
15
Choose a number between 1 and 6:
2
Your balance is: 15
Your last roll was: (1, 1, 3)
You lost 15!
What do you want to bet?
7
Choose a number between 1 and 6:
2
Your balance is: 8
Your last roll was: (3, 6, 3)
You lost 7!
What do you want to bet?
4
Choose a number between 1 and 6:
2
Your balance is: 12
Your last roll was: (5, 6, 2)
You matched 1 dice!
You won 4!
What do you want to bet?
6
Choose a number between 1 and 6:
2
Your balance is: 18
Your last roll was: (4, 4, 2)
You matched 1 dice!
You won 6!
What do you want to bet?
9
Choose a number between 1 and 6:
3
Your balance is: 27
Your last roll was: (1, 3, 5)
You matched 1 dice!
You won 9!
What do you want to bet?
18
Choose a number between 1 and 6:
3
Your balance is: 45
Your last roll was: (3, 6, 2)
You matched 1 dice!
You won 18!
What do you want to bet?
22
Choose a number between 1 and 6:
4
Your balance is: 23
Your last roll was: (5, 2, 3)
You lost 22!
What do you want to bet?
11
Choose a number between 1 and 6:
2
Your balance is: 34
Your last roll was: (2, 1, 1)
You matched 1 dice!
You won 11!
What do you want to bet?
17
Choose a number between 1 and 6:
2
Your balance is: 17
Your last roll was: (5, 3, 4)
You lost 17!
What do you want to bet?
6
Choose a number between 1 and 6:
3
Your balance is: 11
Your last roll was: (1, 2, 5)
You lost 6!
What do you want to bet?
5
Choose a number between 1 and 6:
2
Your balance is: 16
Your last roll was: (3, 2, 4)
You matched 1 dice!
You won 5!
What do you want to bet?
8
Choose a number between 1 and 6:
2
Your balance is: 8
Your last roll was: (4, 4, 6)
You lost 8!
What do you want to bet?
4
Choose a number between 1 and 6:
2
Your balance is: 4
Your last roll was: (3, 4, 5)
You lost 4!
What do you want to bet?
2
Choose a number between 1 and 6:
2
Your balance is: 6
Your last roll was: (5, 6, 2)
You matched 1 dice!
You won 2!
What do you want to bet?
3
Choose a number between 1 and 6:
2
Your balance is: 3
Your last roll was: (5, 4, 1)
You lost 3!
What do you want to bet?
1
Choose a number between 1 and 6:
2
Your balance is: 4
Your last roll was: (6, 5, 2)
You matched 1 dice!
You won 1!
What do you want to bet?
2
Choose a number between 1 and 6:
2
Your balance is: 8
Your last roll was: (2, 2, 1)
You matched 2 dice!
You won 4!
What do you want to bet?
4
Choose a number between 1 and 6:
4
Your balance is: 12
Your last roll was: (6, 6, 4)
You matched 1 dice!
You won 4!
What do you want to bet?
6
Choose a number between 1 and 6:
3 
Your balance is: 18
Your last roll was: (3, 4, 4)
You matched 1 dice!
You won 6!
What do you want to bet?
9
Choose a number between 1 and 6:
2
Your balance is: 36
Your last roll was: (2, 3, 2)
You matched 2 dice!
You won 18!
What do you want to bet?
18
Choose a number between 1 and 6:
3
Your balance is: 18
Your last roll was: (2, 6, 5)
You lost 18!
What do you want to bet?
9
Choose a number between 1 and 6:
3
Your balance is: 27
Your last roll was: (5, 3, 4)
You matched 1 dice!
You won 9!
What do you want to bet?
15
Choose a number between 1 and 6:
3
Your balance is: 42
Your last roll was: (1, 3, 6)
You matched 1 dice!
You won 15!
What do you want to bet?
22
Choose a number between 1 and 6:
3
Your balance is: 86
Your last roll was: (3, 5, 3)
You matched 2 dice!
You won 44!
What do you want to bet?
43
Choose a number between 1 and 6:
3
Your balance is: 43
Your last roll was: (4, 6, 4)
You lost 43!
What do you want to bet?
21
Choose a number between 1 and 6:
3
Your balance is: 22
Your last roll was: (6, 1, 6)
You lost 21!
What do you want to bet?
11
Choose a number between 1 and 6:
3
Your balance is: 11
Your last roll was: (4, 6, 4)
You lost 11!
What do you want to bet?
5
Choose a number between 1 and 6:
3
Your balance is: 16
Your last roll was: (1, 4, 3)
You matched 1 dice!
You won 5!
What do you want to bet?
8
Choose a number between 1 and 6:
3
Your balance is: 24
Your last roll was: (3, 6, 6)
You matched 1 dice!
You won 8!
What do you want to bet?
12
Choose a number between 1 and 6:
3
Your balance is: 36
Your last roll was: (5, 4, 3)
You matched 1 dice!
You won 12!
What do you want to bet?
18
Choose a number between 1 and 6:
3
Your balance is: 18
Your last roll was: (2, 6, 6)
You lost 18!
What do you want to bet?
9
Choose a number between 1 and 6:
3
Your balance is: 9
Your last roll was: (6, 4, 5)
You lost 9!
What do you want to bet?
4
Choose a number between 1 and 6:
3
Your balance is: 5
Your last roll was: (6, 4, 5)
You lost 4!
What do you want to bet?
2
Choose a number between 1 and 6:
3
Your balance is: 3
Your last roll was: (4, 1, 1)
You lost 2!
What do you want to bet?
1
Choose a number between 1 and 6:
3
Your balance is: 2
Your last roll was: (4, 5, 1)
You lost 1!
What do you want to bet?
1
Choose a number between 1 and 6:
1
Your balance is: 3
Your last roll was: (1, 4, 6)
You matched 1 dice!
You won 1!
What do you want to bet?
1
Choose a number between 1 and 6:
1
Your balance is: 4
Your last roll was: (6, 1, 6)
You matched 1 dice!
You won 1!
What do you want to bet?
2
Choose a number between 1 and 6:
2
Your balance is: 2
Your last roll was: (5, 3, 4)
You lost 2!
What do you want to bet?
1
Choose a number between 1 and 6:
1
Your balance is: 1
Your last roll was: (3, 6, 6)
You lost 1!
What do you want to bet?
1
Choose a number between 1 and 6:
3
Your balance is: 3
Your last roll was: (6, 3, 3)
You matched 2 dice!
You won 2!
What do you want to bet?
1
Choose a number between 1 and 6:
2
Your balance is: 5
Your last roll was: (2, 6, 2)
You matched 2 dice!
You won 2!
What do you want to bet?
2
Choose a number between 1 and 6:
3
Your balance is: 3
Your last roll was: (5, 2, 1)
You lost 2!
What do you want to bet?
1
Choose a number between 1 and 6:
1
Your balance is: 4
Your last roll was: (1, 4, 3)
You matched 1 dice!
You won 1!
What do you want to bet?
2
Choose a number between 1 and 6:
1
Your balance is: 2
Your last roll was: (4, 4, 6)
You lost 2!
What do you want to bet?
1
Choose a number between 1 and 6:
2
Your balance is: 3
Your last roll was: (5, 4, 2)
You matched 1 dice!
You won 1!
What do you want to bet?
1
Choose a number between 1 and 6:
1
Your balance is: 4
Your last roll was: (1, 5, 4)
You matched 1 dice!
You won 1!
What do you want to bet?
2
Choose a number between 1 and 6:
1
Your balance is: 2
Your last roll was: (5, 3, 6)
You lost 2!
What do you want to bet?
1
Choose a number between 1 and 6:
1
Your balance is: 5
Your last roll was: (1, 1, 1)
You matched 3 dice!
You won 3!
What do you want to bet?
2
Choose a number between 1 and 6:
3
Your balance is: 3
Your last roll was: (2, 2, 1)
You lost 2!
What do you want to bet?
1
Choose a number between 1 and 6:
1
Your balance is: 4
Your last roll was: (4, 3, 1)
You matched 1 dice!
You won 1!
What do you want to bet?
2
Choose a number between 1 and 6:
2
Your balance is: 2
Your last roll was: (5, 1, 3)
You lost 2!
What do you want to bet?
1
Choose a number between 1 and 6:
1
Your balance is: 3
Your last roll was: (1, 2, 6)
You matched 1 dice!
You won 1!
What do you want to bet?
1
Choose a number between 1 and 6:
1
Your balance is: 4
Your last roll was: (4, 3, 1)
You matched 1 dice!
You won 1!
What do you want to bet?
2
Choose a number between 1 and 6:
2
Your balance is: 2
Your last roll was: (5, 3, 3)
You lost 2!
What do you want to bet?
2
Choose a number between 1 and 6:
2
Your balance is: 0
Your last roll was: (4, 3, 5)
You're out of money! Thanks for playing!
You played 65 turns!
"""
