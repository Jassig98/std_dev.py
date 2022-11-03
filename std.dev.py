# Author: Jasmine Singh
# Github Username: Jassig98
# Date: November 1, 2022
# Description:

class Person():

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

def std_dev(person_list):
    total=0
    for person in person_list:
        total += person.get_age()
    mean_age = total/ len(person_list)

    square_sum = 0
    for person in person_list:
        square_sum += (mean_age - person.get.age()) ** 2

    return (square_sum / len(person_list)) ** 0.5
