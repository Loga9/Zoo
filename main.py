class Zoo:
    def __init__(self, name):
        self.name = name
        self.voliers = []
    
    def get_voliers(self):
        for i in self.voliers:
            print(f'В зоопарке {self.name} есть {i.name}')
        
class Volier:
    def __init__(self, name, biom, area, food_capaciti):
        self.name = name
        self.biom = biom
        self.area = area
        self.animals = []
        self.current_amount_food = 0
        self.food_capaciti = food_capaciti
        
    def add_animal(self, animal):
        if animal.live_volier == False:
            self.animals.append(animal)
            print(f'в вольере {self.name} теперь живёт ещё {animal.name}') 
            animal.live_volier = True
        else:
            print(f'Животное {animal.name} уже и так живёт в вольере')

    def get_info_animals(self):
        for animal in self.animals:
            print(f'в вольере {self.name} живёт {animal.view} по имени {animal.name}')
    
    def get_animal_by_name(self, name):
        for animal in self.animals:
            if animal.name == name:
                return animal 
            else:
                return 0
    
    def delete_animal(self, name):
        info_about_animal = self.get_animal_by_name(name)
        if info_about_animal == 0:
            print(f'В вольере {self.name} животного с таким именем {name} нет')
        else:
            info_about_animal.live_volier = False
            self.animals.remove(info_about_animal)
            print(f'Животное {name} было отселено из вольера {self.name}')
            
    def add_food(self, amount_food):
        self.current_amount_food += amount_food
        if self.current_amount_food > self.food_capaciti:
            unnecessary = self.current_amount_food - self.food_capaciti
            self.current_amount_food -= unnecessary
            print(f'В вольере {self.name} еды {self.current_amount_food} / {self.food_capaciti}, лишнее забери {unnecessary}')
        else:   
            print(f'В вольере {self.name} еды {self.current_amount_food} / {self.food_capaciti}')
    
    def open_feeder(self):
        for animal in self.animals:
            if animal.how_eat != animal.volume_food:
                how_need_eat = animal.volume_food - animal.how_eat
                if self.current_amount_food >= how_need_eat:
                    self.current_amount_food -= how_need_eat
                    animal.how_eat += how_need_eat
                    print(f'Животное по имени {animal.name} в клетке {self.name} наелось {animal.how_eat}/{animal.volume_food}')
                else:
                    animal.how_eat += self.current_amount_food
                    print(f'Животное по имени {animal.name} в клетке {self.name} не наелось {animal.how_eat}/{animal.volume_food}')
            else:
                print(f'Животное по имени {animal.name} в клетке {self.name} уже сыто {animal.how_eat}/{animal.volume_food}')
class Animal:
    def __init__(self, view, biom, area, food, predator, sound, name, volume_food, age):
        self.view = view
        self.biom = biom
        self.area = area
        self.food = food
        self.predator = predator
        self.sound = sound
        self.name = name
        self.volume_food = volume_food
        self.age = age
        self.live_volier = False
        self.how_eat = 0
        
    def Eat(self):
        print("Кушаю", self.food)
    
    def GetSound(self):
        print(self.sound)
    
    def Play(self):
        print(self.view, "по имени", self.name, "играет")
        
animal1=Animal("тигр", "тропики", "10 м2", "мясо", "хищник", "ррр", "Симба", 5, "5")
animal1.Eat()
animal1.GetSound()
animal1.Play()
animal2=Animal("тигр", "тропики", "10 м2", "мясо", "хищник", "ррр", "Пушок", 5, "5")
volier1=Volier("вольер 1", "тропики", 15, 100)
zoo1=Zoo("Зоопарк")
zoo1.voliers.append(volier1)
volier1.add_animal(animal1)
volier1.add_animal(animal2)
volier1.get_info_animals()
result = volier1.get_animal_by_name("Симба")
print(result)
volier1.add_animal(animal2)
volier1.add_food(60)
volier1.add_food(60)
volier1.open_feeder()
volier1.open_feeder()
zoo1.get_voliers()