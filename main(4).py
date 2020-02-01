import datetime
class Territory:

    def __init__(self, date=None, surface=True, title=None, population=1000, dragon=None):
        self.date = date
        self.surface = surface
        self.title = title
        self.population = population
        self.dragon = dragon

    def show(self):
        if self.surface:
            str_surface = "Mountain"
        else:
            str_surface = "Plain"

        return "Title:" + str(self.title) + ', Date: ' + str(self.date) \
        + ', Surface: ' + str_surface + ', Population: ' + str(self.population) + ', Dragon: ' + str(self.dragon) + ";"

    def add(self):
        self.title = input("Write Title: ")
        self.population = int(input("Write Population: "))
        str_surface = input("Write Surface (M/P): ")
        self.dragon = input('Write Dragon: ')
        if str_surface == 'P':
            self.surface = False
        else:
            self.surface = True
        year = int(input("Write Year: "))
        month = int(input("Write Month: "))
        day = int(input("Write Day: "))
        self.date = datetime.date(year, month, day)
        
territories = []
territories.append(Territory(datetime.date(200, 9, 9), True, 'Фолкрит', 1000, 'Алдуин'))
territories.append(Territory(datetime.date(100, 10, 19), False, 'Вайтран', 900, 'Мерриус'))
while True:
    command = input("Write a command \r\n")

    if command == "Add":
        new_territory = Territory()
        new_territory.add()
        territories.append(new_territory)

    if command == "Exit":
        break

    if command.upper() == "SHOW":
        for Territory in territories:
            print(Territory.show())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
