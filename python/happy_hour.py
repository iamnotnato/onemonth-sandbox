#!/usr/bin/env python3
import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people=["Mattan",
	"Chris",
	"Jensen Ackles",
	"Andre 3000",
	"Naveen Andrews",
	"Jensen Atwood",
	"Tyler Bachtel",
	"Penn Badgley",
	"Simon Baker",
	"Christian Bale",
	"Eric Balfour",
	"Eric Bana",
	"Alex Band",
	"Antonio Banderas",
	"Ike Barinholtz",
	"Ben Barnes",
	"Eugen Bauder",
	"William Beckett",
	"Tyson Beckford",
	"David Beckham",
	"Jason Behr",
	"Jonathan Bennett",
	"Sam Bennett ",
	"Dierks Bentley",
	"Gael Garcia Bernal",
	"Jon Bernthal",
	"Wilson Bethel ",
	"Justin Bieber",
	"David Blaine",
	"James Blake",
	"Corbin Bleu",
	"Orlando Bloom",
	"Jon Bon Jovi",
	"Asher Book",
	"David Boreanaz",
	"Tom Bott",
	"Raoul Bova",
	"Bow Wow",
	"Marlon Brando",
	"Adam Brody",
	"Chris Brown",
	"Michel Brown",
	"Justin Bruening",
	"Austin Butler",
	"Gerard Butler",
	"Santiago Cabrera",
	"Bobby Cannavale",
	"Nick Cannon",
	"Robert Carmine",
	"Chris Carmack",
	"Ryan Carnes",
	"Anthony Catanzaro",
	"Gavin Belson",
	"that person you forgot to text back",
	"Kanye West",
	"Samuel L. Jackson"]

random_bar = random.choice(bars)
random_person = random.choice(people)
random_friend = random.choice(people)

if random_friend != random_person:
 random_friend
else:
 random_friend = random.choice(people)

print(f"How about you go to {random_bar} with {random_person} and {random_friend}")
