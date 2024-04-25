class Phone:

    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    def get_attr(self,**kwargs):

        result = [(key,value) for key,value in kwargs.items()]
        print(result)

Iphone = Phone("Iphone-x","Nokia")

Iphone.get_attr(brand = "Iphone", name="Gold")