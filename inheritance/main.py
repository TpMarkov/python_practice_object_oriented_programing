class Animal:
    def __init__(self, name):
        self.number_of_eyes = 2
        self.name = name

    def breathe(self):
        print("Normal breathe!")


class Fish(Animal):

    def __init__(self, name):
        super().__init__(name)

    def breathe(self):
        super().breathe()
        print("Breathe for fish")


first_cat = Fish("Tom")
first_cat.breathe()
