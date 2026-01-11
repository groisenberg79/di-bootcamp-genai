# Part 1
# You will have to create two classes:
# Human
# Queue

# Human
# Represents a citizen of the city, it has the following attributes: id_number (str), name (str), age (int), priority (bool) and blood_type (str). Its blood type can be “A”, “B”, “AB” or “O”.
# This class has no methods.

# Queue
# Represents a queue of humans waiting for their vaccine.
# It has the following attribute : humans, the list containing the humans that are waiting. It is initialized empty.

# This class is useful to manage who will get vaccinated in priority. It has the following methods:
# add_person(self, person) : Adds a human to the queue, if he is older than 60 years old or a priority person, put him at the beginning of the list (at index 0) before every other.

# find_in_queue(self, person) : Returns the index of a human in the queue.
# swap(self, person1, person2): Swaps person1 with person2.
# get_next(self) : Returns the next human waiting in the queue. The next human should be the one located at the index 0 in the list.
# get_next_blood_type(self, blood_type) : Returns the first human with this specific blood type.
# sort_by_age(self) : Sorts the queue
# first the priority people
# then, the older people
# then the younger people
# Every human returned by get_next and get_next_blood_type is removed from the list.
# Those functions return None if the list is empty (ie. no one in the list).

# Bonus: Don’t use any of the following built-in methods: list.insert, list.pop, list.index, list.sort, sorted.

# Part 2
# Human
# Create an attribute family for the Human class.
# Initialized as empty, family is a list of all the humans that are living in the same house with this human.
# Add a method add_family_member(self, person) that adds the person to this human’s family and this human to the person’s family.

# Queue
# Add the rearrange_queue(self) method to the Queue class, so that there won’t be two members of the same family one after the other in the line.
from __future__ import annotations

class Human:
    def __init__(self, id_number: str, name: str, age: int, priority: bool, blood_type: str, family: list[Human] = None):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = [] if family is None else family

    def add_family_member(self, person: Human) -> None:
        if person is self:
            return
        if person not in self.family:
            self.family.append(person)
        if self not in person.family:
            person.family.append(self)

class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person: Human) -> None:
        if person.age >= 60 or person.priority:
            i = 0
            while i < len(self.humans) and (self.humans[i].age >= 60 or self.humans[i].priority):
                i += 1
            self.humans.insert(i, person)
        else:
            self.humans.append(person)
    
    def find_in_queue(self, person: Human) -> int:
        return self.humans.index(person)

    def swap(self, person1: Human, person2: Human) -> None:
        index1 = self.humans.index(person1)
        index2 = self.humans.index(person2)
        self.humans[index1] = person2
        self.humans[index2] = person1

    def get_next(self) -> Human|None:
        if self.humans == []:
            return None
        return self.humans.pop(0)

    def get_next_blood_type(self, blood_type: str) -> Human|None:
        """
        Returns the first human with this specific blood type, None if no one has the blood type or the list is empty
        :param blood_type: a blood type (A, B, AB or O)
        :type blood_type: str
        """
        for person in self.humans:
            if person.blood_type == blood_type:
                return self.humans.pop(self.humans.index(person))
        return None     # if no one has blood_type
    
    def sort_by_age(self) -> None:
        # sort persons according to age in descending order
        self.humans.sort(reverse=True, key=lambda x: x.age)
        # sort persons according to priority in descending order (True -> False),
        # preserving age order (if not overriden by priority) 
        self.humans.sort(reverse=True, key=lambda x: x.priority)
        
    def find_another_family_from_index(self, i: int, family: list[Human]) -> int:
        if i < len(self.humans) - 1:
            # find first index > i that is NOT in family
            for j in range(i + 1, len(self.humans)):
                if self.humans[j] not in family:
                    return j
        return -1

    def rearrange_queue(self) -> None:
        i = 0
        while i < len(self.humans) - 1:
            if self.humans[i + 1] in self.humans[i].family:
                j = self.find_another_family_from_index(i + 1, self.humans[i].family)
                if j != -1:
                    self.swap(self.humans[i + 1], self.humans[j])
            i += 1







                





