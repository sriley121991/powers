import sys
import time
from random import randint

enemies = ["Goblin", "Giant", "Troll", "Bandit"]
weapons = ["Sword", "Mace", "Bow", "Club", "Spear"]
elements = ["Earth", "Water", "Fire", "Wind"]


def get_computer_element():
	return elements[randint(0,3)]

def get_player_input(request):
	return input(request)

def start_game():
	print("Welcome to Powers, a game where you get to battle with the elements!")
	print("A fierce enemy faces you. They have the power of Earth, Wind, Water")
	print("or Fire. It's up to you defeat them. To do so, you must choose the ")
	print("element that beats the one your enemy uses. Earth beats Water. Water")
	print("beats Fire. Fire beats Wind. Wind beats Earth. The future is up to")
	print("you. Protect the world of Powers!")
	check_for_new_round("Are you ready to play? Y/N ")

def start_new_round(request):
	enemy = enemies[randint(0, 3)]
	weapon = weapons[randint(0,4)]
	computer_element = get_computer_element()
	print("You are faced by a {}! He weilds a {} and advances towards you. You".format(
		enemy, weapon))
	print("can tell that he has an affinity with one of the elements, but you")
	print("can't determine which one. Your only option is to hit him with an ")
	print("element of your choosing!")
	check_victory_conditions(request, computer_element, enemy)

def check_for_new_round(request):
	response = get_player_input(request)
	if response.upper() == "Y":
		start_new_round("Which element would you like to use (Earth, Wind, Water, or Fire)? ")
	elif response.upper() == "N":
		exit_game()
	else:
		print("That is not a valid option. Please enter Y or N.")
		check_for_new_round(request)

def exit_game():
	print("Thank you for playing!")
	time.sleep(1)
	sys.exit()

def check_victory_conditions(request, computer_element, enemy):
	player_element = get_player_input(request).lower()
	print("You shoot off some {} magic!".format(player_element))
	if computer_element.lower() == player_element:
		print("However, your enemy seems to be unaffected. You must be using")
		print("the same element!")
		check_victory_conditions(request, computer_element, enemy)
	elif player_element == "earth":
		earth_conditions(request, computer_element, enemy)
	elif player_element == "fire":
		fire_conditions(request, computer_element, enemy)
	elif player_element == "wind":
		wind_conditions(request, computer_element, enemy)
	elif player_element == "water":
		water_condidtions(request, computer_element, enemy)
	else:
		print("That is not a valid element! Try again!")
		check_victory_conditions(request, computer_element, enemy)


def earth_conditions(request, computer_element, enemy):
	if computer_element == "Water":
		print("You've defeated the {}!".format(enemy))
		print("They must have been using {} magic!".format(computer_element))
		check_for_new_round("Would you like to play again? Y/N ")
	elif computer_element == "Wind":
		print("The enemy laughs at your attack, and then counters with {}".format(
			computer_element))
		print("magic! You've been defeated!")
		check_for_new_round("Would you like to try again? Y/N ")
	elif computer_element == "Fire":
		print("The enemy takes slight damage, but nothing serious. Maybe you")
		print("should try a new element!")
		check_victory_conditions(request, computer_element, enemy)


def fire_conditions(request, computer_element, enemy):
	if computer_element == "Wind":
		print("You've defeated the {}!".format(enemy))
		print("They must have been using {} magic!".format(computer_element))
		check_for_new_round("Would you like to play again? Y/N ")
	elif computer_element == "Water":
		print("The enemy laughs at your attack, and then counters with {}".format(
			computer_element))
		print("magic! You've been defeated!")
		check_for_new_round("Would you like to try again? Y/N ")
	elif computer_element == "Earth":
		print("The enemy takes slight damage, but nothing serious. Maybe you")
		print("should try a new element!")
		check_victory_conditions(request, computer_element, enemy)


def wind_conditions(request, computer_element, enemy):
	if computer_element == "Earth":
		print("You've defeated the {}!".format(enemy))
		print("They must have been using {} magic!".format(computer_element))
		check_for_new_round("Would you like to play again? Y/N ")
	elif computer_element == "Fire":
		print("The enemy laughs at your attack, and then counters with {}".format(
			computer_element))
		print("magic! You've been defeated!")
		check_for_new_round("Would you like to try again? Y/N ")
	elif computer_element == "Water":
		print("The enemy takes slight damage, but nothing serious. Maybe you")
		print("should try a new element!")
		check_victory_conditions(request, computer_element, enemy)

def water_condidtions(request, computer_element, enemy):
	if computer_element == "Fire":
		print("You've defeated the {}!".format(enemy))
		print("They must have been using {} magic!".format(computer_element))
		check_for_new_round("Would you like to play again? Y/N ")
	elif computer_element == "Earth":
		print("The enemy laughs at your attack, and then counters with {}".format(
			computer_element))
		print("magic! You've been defeated!")
		check_for_new_round("Would you like to try again? Y/N ")
	elif computer_element == "Wind":
		print("The enemy takes slight damage, but nothing serious. Maybe you")
		print("should try a new element!")
		check_victory_conditions(request, computer_element, enemy)



start_game()