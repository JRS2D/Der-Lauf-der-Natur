__author__​ ​=​ ​"7714256 Laterza"

class Lebewesen:
	__init__(self, population):
		if population > 1:
			self.population = population


class Pflanze(Lebewesen):
	def __init__(self, groesse, minimale_groesse, maximale_groesse):
		self.groesse = groesse
		self.minimale_groesse = minimale_groesse
		self.maximale_groesse = maximale_groesse


	def sterben(groesse):
		return 0


class Tier(Lebewesen):
	def __init__(self, alter, hunger, gesundheit):
		self.alter = alter
		self.hunger = hunger
		self.gesundheit = gesundheit


	def fressen(self, hunger_gedeckt):
		return 0


	def futtersuche(self, art_des_futters):
		pass


	def sterben(self):
		pass


	def vermehren(self, population):
		pass


class Habitat:
	def __init__(self, verfuegbare_flaeche, pflanze, tier):
		self.verfuegbare_flaeche = verfuegbare_flaeche
		self.pflanze = pflanze
		self.tier = tier


	def berechne_verfuegbare_flaeche(self, flaeche):
		return flaeche


class Main:
	def __init__(self, habitat):
		self.habitat = habitat


	def main(self):
		pass