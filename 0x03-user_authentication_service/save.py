
class Student:

    def __init__(self, name, score):

        self.name = name
        self.score = score

    @property
    def full_info(self):

        return "{} Score: {}".format(self.name, self.name)

Dimka = Student("Dimka",90)
Divine= Student( "Divine",95)
print(Dimka.full_info)
print(Divine.full_info)