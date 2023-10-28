import random

places = ["Naivasha",
	  "Meru"]

activities = ["Hiking",
	      "Jumping"]

place = random.choice(places)
activity  = random.choice(activities)

print(f"How about {place} to go {activity} ?")
