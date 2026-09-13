# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    # dont change initial code
    def __str__(self):
        return f"{self.name} ({self.height} cm)"

class Room:
    def __init__(self):
        self.amount = 0
        self.room = []

    def add(self, person: Person):
        # adds the person given as an argument to the room.
        self.room.append(person)
        self.amount += 1

    def is_empty(self):
        # returns True or False depending on whether the room is empty
        return self.amount == 0

    def print_contents(self):
        sum_height = sum(person.height for person in self.room)
        print(f"There are {self.amount} persons in the room, and their combined height is {sum_height} cm")
        for person in self.room:
            print(person)

    def shortest(self):
        # return the shortest person in the room
        # If the room is empty, the method should return None. 
        shortest_person = None
        shortest_height = None
        for person in self.room:
            if shortest_height == None or person.height < shortest_height:
                shortest_height = person.height
                shortest_person = person

        # if initial code did not be changed, this return right
        return shortest_person

    def remove_shortest(self):
        # remove the shortest Person object from the room and return the reference to the object. 
        # If the room is empty, the method should return None.
        shortest_person = self.shortest()
        if shortest_person == None:
            return None
        for person in self.room:
            if person.name == shortest_person.name:
                self.room.remove(person)
                self.amount -= 1
                return person
        



if __name__ == "__main__":
    room = Room()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))

    print()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    print()

    room.print_contents()
    