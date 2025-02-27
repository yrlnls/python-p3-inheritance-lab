#!/usr/bin/env python

from user import User
import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Python Basics", "OOP", "Data Structures", "Algorithms"]  

    def teach(self):
        random_index = random.randint(0, len(self.knowledge) - 1)
        return self.knowledge[random_index]
