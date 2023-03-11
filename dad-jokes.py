import requests
from pyfiglet import figlet_format
from termcolor import colored
from random import choice

colors = (
	"red", 
	"green", 
	"yellow", 
	"blue", 
	"magenta", 
	"cyan", 
	"light_grey", 
	"dark_grey", 
	"light_red", 
	"light_green", 
	"light_yellow", 
	"light_blue", 
	"light_magenta", 
	"light_cyan"
)

rand_color1 = choice(colors)
rand_color2 = choice(colors)

playing = True

header = colored(figlet_format("dad jokes"), color=rand_color1)
print(header)

while playing == True:

	term = input("What would you like to search for? (press 'q' to quit) ")

	if term == "q":
		print("Thanks for playing!")
		playing = False

	else:

		if not term:
			term = input("Please try again. What would you like to search for? ")
		url = "https://icanhazdadjoke.com/search"

		res = requests.get(
			url,
			headers={"Accept": "application/json"},
			params={"term": term}
		).json()

		num_of_jokes = res["total_jokes"]
		results = res["results"]

		if num_of_jokes > 1:
			print(f"There are {num_of_jokes} jokes about '{term}'. Here's one:")
			joke = choice(results)["joke"]
			print(colored(joke, color=rand_color2))
		elif num_of_jokes == 1:
			print(f"I found one joke about '{term}':")
			joke = results[0]['joke']
			print(colored(joke, color=rand_color2))
		else:
			msg = f"Sorry, there are no jokes about '{term}'."
			print(colored(msg, color=rand_color2))




