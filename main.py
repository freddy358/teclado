class Student:

    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student("Freddy", [15, 20, 25, 30, 35])

print(student_one.name, "avegare is: ", student_one.average())


class Movie:
    def __init__(self, movie_name, movie_produces):
        self.name = movie_name
        self.director = movie_produces

    def print_info(self):
        print("<<{}>>".format(self.name) + " by " + self.director)


my_movie = Movie('The Matrix', 'Wachowski')

my_movie.print_info()


class Garage:
    def __init__(self):
        self.cars = []

ford = Garage()

ford.cars.append("Fiesta")

print(ford.cars)