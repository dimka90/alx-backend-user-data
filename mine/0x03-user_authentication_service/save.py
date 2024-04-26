
class Student:

    def __init__(self, name, score):

        self.name = name
        self.score = score

    @property
    def full_info(self):

        return "{} Score: {}".format(self.name, self.name)

    def get_student(self, **kwargs):
        attrs, values = [], []
        for attr, value in kwargs.items():
            if not hasattr(self, attr):
                print(f" {attr} not in Student")
            else:
                attrs.append(getattr(self,attr))
                values.append(value)
                print(f"Attri:({attr}) Value:({value})")
        print(attrs)
        print(values)


Dimka = Student("dimka", 90)

Dimka.get_student(name = "dimka", score = 90)

for attr, values in kwargs.items():
            if not hasattr(User, attr):
                raise InvalidRequestError()

        user = self._session.query(User).filter_by(**kwargs).one()
        if not user:
            raise InvalidRequestError
        return user

        if not kwargs:
            raise InvalidRequestError
        for attr, values in kwargs.items():
            if not hasattr(User, attr):
                raise InvalidRequestError

        user = self._session.query(User).filter_by(**kwargs).one()
        if not user:
            raise InvalidRequestError
        return user
