#!/usr/bin/python
import random

pizza = ['Pizza is what gives a programmer his power. It\'s an energy source created by tomato sauce, cheese, and crust. It nourishes us and uplifts us. It binds the software together.',
("You wanna buy some deep dish pizza?\n"
" You don\'t want to sell me deep dish pizza.\n"
"Uh, I don\'t wanna sell you deep dish pizza.\n"
" You want to go home and cook NY style pizza.\n"
"I wanna go home and cook NY style pizza."),
"Metro Chicago. You will never find a more wretched hive of deep dish pizza. We must order spaghetti.",
"If this is a pizza shop, where is the NY style pizza? Programmers, tear this shop apart until you've found the recipes. And bring me the pizza chefs, I want them alive!",
"That's no pizza!",
"Awww! But I was going into Tosche Station to pick up some pizza!!!",
"Only a master of deep-dish pizza, Darth.",
"I find your lack of NY pizza disturbing.",]

print pizza[int(random.random() * len(pizza))]
