# Practice_17

# Library
from os import system as sys
from termcolor2 import colored
from pyfiglet import figlet_format

# Clear Terminal
sys('clear')

# Intro
print(colored(figlet_format("Exercises Part 1"), color='cyan'))
print(colored('=====================================================================', color='red'))
print(colored('Question Number ===> 17', color='blue'))
print(colored('// Be Sure To Read The README File To See The Question //', color='blue'))
print('                                            ')

# Value
d1 = {'name':'Hamid', 'age':25}
d2 = {'job':'baker'}

# Update Dictionary 
d1.update(d2)

# Print Dictionary
print(d1)

# Finish
# Create By Moein Heshmati
