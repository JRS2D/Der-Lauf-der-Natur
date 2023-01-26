__author__ = "7714256 Laterza"

import random

class Creature:
	def __init__(self, population):
		if population > 1:
			self.population = population


class Plant(Creature):
	def __init__(self, name, type, population, size, minimal_size, maximal_size):
		self.name = name
		self.type = type
		self.size = size
		self.minimal_size = minimal_size
		self.maximal_size = maximal_size
		super().__init__(population)


	def death(size):
		return 0


class Tree(Plant):
	def __init__(self, name, population, size, minimal_size, maximal_size, height, leaves, fruit):
		self.height = height
		self.leaves = leaves
		self.fruit = fruit
		super().__init__(name, "Baum", population, size, minimal_size, maximal_size)


	def multiply(population, fruit):
		pass


class Mushroom(Plant):
	def __init__(self, name, population, size, minimal_size, maximal_size, spore):
		self.spore = spore
		super().__init__(name, "Pilz", population, size, minimal_size, maximal_size)


	def multiply(population):
		pass


class Shrub(Plant):
	def __init__(self, name, population, size, minimal_size, maximal_size, berries):
		self.berries = berries
		super().__init__(name, "Strauch", population, size, minimal_size, maximal_size)


class Animal(Creature):
	def __init__(self, name, population, age, hunger, health):
		self.name = name
		self.age = age
		self.hunger = hunger
		self.health = health
		super().__init__(population)


	def forage(self, type_of_feed, plants):
		if random.choice([True, True, True, False]):
			plant = random.choice(plants)
			if plant.size != 0 and plant.population > 0:
				match plant.type:
					case "Baum":
						if plant.fruit != 0:
							plant.fruit -= 1
							if self.hunger < 10:
								self.hunger = 0
							else:
								self.hunger -= 10
					case "Strauch":
						for i in range(random.randint(1, plant.berry)):
							plant.berry -= 1
							self.hunger -= 2
					case "Pilz":
						plant.size -= 1
						if plant.size == 0:
							plant.population -= 1
			else:
				self.hunger += 5


	def death(self):
		if self.age == 0:
			self.population -= 1
		elif self.hunger == 100:
			self.population -= 1


	def breed(self, population):
		choice = random.choice([True, False])
		if choice:
			return population + random.randint(1, 5)
		return population


class Herbivore(Animal):
	def __init__(self, name, population, age, hunger, health):
		self.type_of_feed = "herbivore"
		super().__init__(name, population, age, hunger, health)


class Carnivore(Animal):
	def __init__(self, name, population, age, hunger, health):
		self.type_of_feed = "carnivore"
		super().__init__(name, population, age, hunger, health)


	def hunt(self, potential_prey):
		if random.choice([True, True, True, False]):
			potential_prey = random.choice(potential_prey)
			danger = random.randint(0, 101)
			if danger > 0:
				self.health -= danger
				if self.health > 0:
					if potential_prey.type_of_feed == "herbivore":
						if self.hunger < 50:
							self.hunger = 0
						else:
							self.hunger -= 50
						return potential_prey.population - 1
					else:
						if self.name != potential_prey.name:
							if self.hunger < 50:
								self.hunger = 0
							else:
								self.hunger -= 50
							return potential_prey.population - 1
						else:
							self.hunger -= 20
							return potential_prey.population
				else:
					self.population -= 1
					return potential_prey.population
		else:
			return potential_prey.population


class Omnivore(Herbivore, Carnivore):
	def __init__(self, name, population, age, hunger, health):
		self.type_of_feed = "omnivore"
		super().__init__(name, population, age, hunger, health)



class Habitat:
	def __init__(self, available_space):
		self.available_space = available_space
		# animals
		self.carnivores = []
		self.herbivores = []
		self.omnivores = []
		# plants
		self.trees = []
		self.shrubs = []
		self.mushrooms = []


	def get_initial_population(self, type_of_creature):
		initial_available_space = self.available_space
		if type_of_creature == "animal":
			return random.randint(1, 21)
		elif type_of_creature == "plant":
			if ((initial_available_space / 100) * 99) < self.available_space:
				return random.randint(1, 101)
		else:
			print("Unknown type of creature")
			return 0


	def generate_initial_life(self):
		#TODO Flaechenberechnung
		# initialisation of plants
		population = self.get_initial_population("plant")
		hazel = Tree("Hasselnussbaum", population, 1, 1, 300, 1, 0, 0)
		population = self.get_initial_population("plant")
		oak = Tree("Eiche", population, 1, 1, 1500, 3500, 0, 0)
		population = self.get_initial_population("plant")
		chestnut_tree = Tree("Kastanienbaum", population, 1, 1, 800, 3000, 0, 0)
		population = self.get_initial_population("plant")
		self.available_space -= population
		chestnut_boletus = Mushroom("Maronen-Roehrling", population, 1, 1, 30, random.randint(1, 20))
		population = self.get_initial_population("plant")
		self.available_space -= population
		chanterelle = Mushroom("Pfifferling", population, 1, 1, 8, random.randint(1, 20))
		population = self.get_initial_population("plant")
		self.available_space -= population
		parasol_mushroom = Mushroom("Parasolpilz", population, 1, 1
		, 35, random.randint(1, 20))
		population = self.get_initial_population("plant")
		blueberry_shrub = Shrub("Blaubeerstrauch", population, 10, 1, 200, 100)
		population = self.get_initial_population("plant")
		blackberry_shrub = Shrub("Brombeerstrauch", population, 10, 1, 200, 100)
		population = self.get_initial_population("plant")
		currants_shrub = Shrub("Johannisbeerstrauch", population, 10, 1, 200, 100)
		self.plants = [
			hazel, oak, chestnut_tree,
			chestnut_boletus, chanterelle, parasol_mushroom,
			blueberry_shrub, blackberry_shrub, currants_shrub
			]
		# initialisation of animals
		# age is counted down
		population = self.get_initial_population("animal")
		wolf = Carnivore("Wolf", population, 15, 0, 100)
		population = self.get_initial_population("animal")
		fox = Carnivore("Fuchs", population, 4, 0, 100)
		population = self.get_initial_population("animal")
		deer = Herbivore("Reh", population, 15, 0, 100)
		population = self.get_initial_population("animal")
		squirrel = Herbivore("Eichhoernchen", population, 3, 0, 100)
		population = self.get_initial_population("animal")
		insects = Herbivore("Insekten", population, 1, 0, 1000)
		population = self.get_initial_population("animal")
		mouse = Omnivore("Maus", population, 2, 0, 100)
		population = self.get_initial_population("animal")
		rat = Omnivore("Ratte", population, 3, 0, 100)
		population = self.get_initial_population("animal")
		boar = Omnivore("Wildschwein", population, 6, 0, 100)
		self.animals = [wolf, fox, deer, squirrel, insects, mouse, rat, boar]


class Main:
	def __init__(self):
		self.habitat = Habitat(random.randint(10000, 1000001))
		self.aktueller_tag = 0


	def user_input_habitat(self):
		welcome_message = "Herzlich willkomen zur Sandbox Lauf-der-Natur. " 
		welcome_message += "Das gesammte Spiel ist fuer die Konsole ausgelegt. "
		welcome_message += "Du hast jetzt die Moeglichkeit dein Habitat anzupassen "
		welcome_message += "oder bei den Standardwerten zu bleiben. "
		welcome_message += "Gerne darfst du auch das Habitat um weitere Tiere und "
		welcome_message += "Pflanzen erweitern. \n\n"
		welcome_message += "Okay. Los geht's \n Das sind die Pflanzen bisher: \n"
		plants = self.habitat.plants
		for i in range(plants):
			plant_info = f"Name = {plants[i].name}\nTyp: {plants[i].type}\n"
			plant_info += f"Anzahl: {plants[i].population}\nGroesse: {plants[i].sizes}\n"
			plant_info += f"Minmale Groesse: {plants[i].minimal_size}\n"
			plant_info += f"Maxmale Groesse: {plants[i].maximal_size}\n"
			if plants[i].type == "Baum":
				plant_info += f"Hoehe: {plants[i].height}\n"
				plant_info += f"Blaetter: {plants[i].leaves}\n"
				plant_info += f"Fruechte: {plants[i].fruit}\n"
			elif plants[i].type == "Pilz":
				plant_info += f"Sporen: {plants[i].spore}"
			elif plants[i].type == "Strauch":
				plant_info += f"Beeren: {plants[i].berries}"


	def simulate(self, days):
		for i in range(days):
			pass


	def round(self, einheit):
		days_to_simulate = 1
		match einheit:
			case "t":
				self.aktueller_tag += 1
				print(f"Tag {self.aktueller_tag}")
			case "w":
				days_to_simulate = 7
				self.aktueller_tag += 7
				print(f"Tag {self.aktueller_tag}")
			case "m":
				days_to_simulate = 28
				self.aktueller_tag += 28
				print(f"Tag {self.aktueller_tag}")
			case "j":
				days_to_simulate = 84
				self.aktueller_tag += 84
		self.simulate(days_to_simulate)


	def main(self):
		self.habitat.generate_initial_life()
		print(self.habitat.plants)
		self.habitat.animals[0].hunt(self.habitat.animals)
		while True:
			print("Wie viel Zeit soll eine Runde simulieren?")
			print("Auswahl:")
			print("Tag | Woche | Monat | Jahreszeit")
			print("Tag = t, Woche = w, Monat = m, Jahreszeit = j")
			einheit = input("Eingabe: ")
			print(einheit)
			match einheit:
				case "t" | "w" | "m" | "j":
					break
		self.round(einheit)


if __name__ == "__main__":
	main = Main()
	main.main()