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
