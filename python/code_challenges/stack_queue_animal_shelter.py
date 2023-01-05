from code_challenges.queue import Queue, Node, InvalidOperationError


class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal):
        if animal.type != "dog" and animal.type != "cat":
            raise InvalidOperationError
        if animal.type == "dog":
            self.dogs.enqueue(animal)
        if animal.type == "cat":
            self.cats.enqueue(animal)

    def dequeue(self, pref=""):
        if pref == "dog":
            return self.dogs.dequeue()
        if pref == "cat":
            return self.cats.dequeue()


class Dog:

    def __init__(self):
        self.type = "dog"

    def __repr__(self):
        return "dog"


class Cat:

    def __init__(self):
        self.type = "cat"

    def __repr__(self):
        return "cat"
