__author__ = "7714256 Laterza"

class Lebewesen:
	def __init__(self, population):
		if population > 1:
			self.population = population


class Pflanze(Lebewesen):
	def __init__(self, population, groesse, minimale_groesse, maximale_groesse, habitat):
		self.habitat = habitat
		self.groesse = groesse
		self.minimale_groesse = minimale_groesse
		self.maximale_groesse = maximale_groesse
		super().__init__(population)


	def sterben(groesse):
		return 0


class Baum(Pflanze):
	def __init__(self, population, groesse, minimale_groesse, maximale_groesse, habitat, hoehe, blaetter, fruechte):
		self.hoehe = hoehe
		self.blaetter = blaetter
		self.fruechte = fruechte
		super().__init__(population, groesse, minimale_groesse, maximale_groesse, habitat)


	def vermehren(population, fruechte):
		pass


class Pilz(Pflanze):
	def __init__(self, population, groesse, minimale_groesse, maximale_groesse, habitat, sprossen):
		self.sprossen = sprossen
		super().__init__(population, groesse, minimale_groesse, maximale_groesse, habitat)


	def vermehren(population):
		pass


class Strauch(Pflanze):
	def __init__(self, population, groesse, minimale_groesse, maximale_groesse, habitat, beeren):
		self.beeren = beeren
		super().__init__(population, groesse, minimale_groesse, maximale_groesse, habitat)


class Tier(Lebewesen):
	def __init__(self, population, alter, hunger, gesundheit, habitat):
		self.habitat = habitat
		self.alter = alter
		self.hunger = hunger
		self.gesundheit = gesundheit
		super().__init__(population)


	def fressen(self, hunger_gedeckt):
		return 0


	def futtersuche(self, art_des_futters):
		pass


	def sterben(self):
		pass


	def vermehren(self, population):
		pass


class Pflanzenfresser(Tier):
	def __init__(self, population, alter, hunger, gesundheit, habitat):
		self.art_des_futters = "vegan"
		super().__init__(population, alter, hunger, gesundheit, habitat)


class Fleischfresser(Tier):
	def __init__(self, population, alter, hunger, gesundheit, habitat):
		self.art_des_futters = "fleisch"
		super().__init__(population, alter, hunger, gesundheit, habitat)


	def jagen(self):
		pass


class Allesfresser(Pflanzenfresser, Fleischfresser):
	def __init__(self, population, alter, hunger, gesundheit, habitat):
		self.art_des_futters = "vollkost"
		super().__init__(population, alter, hunger, gesundheit, habitat)



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
		self.aktueller_tag = 0


	def round(self, einheit):
		days_to_simulate = 1
		match einheit:
			case "day":
				self.aktueller_tag += 1
				print(f"Tag {self.aktueller_tag}")
			case "week":
				days_to_simulate = 7
				self.aktueller_tag += 7
				print(f"Tag {self.aktueller_tag}")
			case "month":
				days_to_simulate = 28
				self.aktueller_tag += 28
				print(f"Tag {self.aktueller_tag}")
			case "season":
				days_to_simulate = 84
				self.aktueller_tag += 84


	def main(self):
		pass


if __name__ == "__main__":
	main = Main()
	main.main()