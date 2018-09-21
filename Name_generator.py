import random

women_name = ("Joanna", "Ewa", "Izabela", "Katarzyna", "Anna", "Magda", "Zofia", "Iga")
women_surname = ("Kowalska", "Dylewska", "Mielecka", "Grzesiuk", "Dublewska", "Nowak", "Ibisz", "Kulesza")

men_name = ("Tomasz", "Bartosz", "Janusz", "Damian", "Oskar", "Tobiasz", "Aleksander", "Marcin")
men_surname = ("Kowalski", "Pioro", "Dawidziuk", "Piaseczny", "Kuberski", "Nowak", "Grzesiuk", "Bigos")


while True:
    gender = input("Choose gender: ")
    if gender == "w":
        a = random.choice(women_name) + " " + random.choice(women_surname)
        print a
    elif gender == "m":
        b = random.choice(men_name) + " " + random.choice(men_surname)
        print b
    else:
        print "Podaj poprawna litere"

