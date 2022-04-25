from abc import ABC, abstractmethod


class LivingBeing(ABC):
    """
        abstract class, all living being has its methods by default
    """

    def __init__(self):
        self.alive: bool = True

    @abstractmethod
    def feed(self):
        # this method has to be implemented
        pass

    def status(self):
        # this can't be implemented but is inherited
        print(f'is alive = {self.alive}')


class Animal(LivingBeing):
    """
        1: extends from ABC witch means is an Abstract Clas
        2: extends from LivingBeing, then is has its feed
    """

    @abstractmethod
    def move(self):
        pass


class Carnivorous(Animal):
    """
        extends from Animal, so it has to implement ALL! abstract methods
        (Animal and LivingBeing abstract methods)
    """

    def __init__(self):
        print('Carnivorous')
        super().__init__()

    def feed(self):
        if self.alive:
            print('I feed by eating other animals')

    def move(self):
        if self.alive:
            print('I can run, fly or swim')


class Herbivorous(Animal):
    """
        extends from Animal, so it has to implement ALL! abstract methods
        (Animal and LivingBeing abstract methods)
     """

    def __init__(self):
        print('Herbivorous')
        super().__init__()

    def feed(self):
        if self.alive:
            print('I feed by eating plats')

    def move(self):
        if self.alive:
            print('I can run, fly or swim')


class Plant(LivingBeing):
    """
        extends from LivingBeing, so, it has to implement feed method
    """

    def __init__(self):
        print('PLANT')
        super().__init__()

    def feed(self):
        if self.alive:
            print('feeding through sun light')

    '''def status(self):  # cant be over written
        print('plat is alive: ', self.status())'''


if __name__ == "__main__":
    plant = Plant()
    carnivorous = Carnivorous()
    herbivorous = Herbivorous()

    living_beings = [plant, carnivorous, herbivorous]

    for being in living_beings:
        print(being.__str__())
        if hasattr(being, 'move'):
            being.move()
        if hasattr(being, 'status'):
            being.status()
        being.feed()
        print('')







