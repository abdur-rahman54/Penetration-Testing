#!/bin/python3

#importing
#print ("Importing is important")

import sys #system funtion and parameters

from datetime import datetime as dt
print(dt.now())


def new_line():
	print('\n')
new_line()

#Advanced string
print("Advanced String")

sentence = "This is advance sentence"


sp = sentence.split() #split sentence by delimiter (space)
print (sp)
jp = '_'.join(sp)
print (jp)

letter = "a"
word = "Apple"
word_two = "Bingo"
print(letter in word)
print(letter.lower() in word.lower())
print((letter.lower() in word.lower()) and not (letter.lower() in word_two.lower()))

too_much_space = "      Hello         "
print(too_much_space.strip()) #deafult is space

full_name = "bdur Rahman"
full_name = full_name.replace("bdur", "Abdur")
print(full_name)
print(full_name.find("Rahman"))
nbr = full_name.find("Rahman")
print(full_name[nbr:])

movie = "The Hangover"
print("My favorite movie is {}.".format(movie))

def favorite_book(title, author):
	fav = "My favorite book is \"{}\", which is writen by {}.".format(title, author)
	return fav

print(favorite_book('lord', 'king'))

new_line()

#Dictionaries
print("Dictionaries are keys and values.")
drinks = {"White Russians": 7, "Old Fashion": 10, "Lemon Drop": 8, "Buttery Nipple": 6}
print (drinks)

employees = {"Finance": ["bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr", "Mort"]}

employees ['Legal'] = ["Mr Frank", "Julean"]

employees.update({"Sales": ["Andie", "Ollie"]})

print (employees)

drinks["White Russians"] = 8 #update the value from inside of drinks
print (drinks)

print(drinks.get("Buttery Nipple"))
print(employees["HR"])

#list and dictionaries

movies = ["When Harry met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

person = ["Heath", "Bob", "Leah", "Jeff"]

combine = zip(movies, person)
#print(list(combine))

new_line()

movie_dictionary = {key: value for key, value in combine}
print(movie_dictionary)





































