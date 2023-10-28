import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
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
