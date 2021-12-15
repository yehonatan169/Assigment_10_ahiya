import json

class Address:
    def __init__(self, country, city, street, number):
        self.country = country
        self.city = city
        self.street = street
        self.number = number
    def __repr__(self):
        return self.street + ', '+str(self.number)+', '+self.city

class Student:
    def __init__(self, id, first_name, last_name, year, address, future_courses, grades):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.address = address
        self.future_courses = future_courses
        self.grades = grades

def load_student(dict):
    if 'id' in dict:
        return Student(**dict)
    if 'country' in dict:
        return Address(**dict)
    return dict

with open('students.json', 'r') as file:
    list_of_stud_obj = json.load(file, object_hook=load_student)['students']

for s in list_of_stud_obj:
    print(s.first_name, s.last_name, s.address)


