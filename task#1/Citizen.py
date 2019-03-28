class Citizen:

    def __init__(self, name="John", second_name="Doe"):
        self.firstName = name
        self.secondName = second_name
        self.age = 18
        self.nationality = ""
        self.address = ""

    def getFirstName(self):
        return self.firstName

    def getSecondName(self):
        return self.secondName

    def getAge(self):
        return self.age

    def getNationality(self):
        return self.nationality

    def getAddress(self):
        return self.address

    def setFirstName(self, first_name):
        self.firstName = first_name

    def setSecondName(self, second_name):
        self.secondName = second_name

    def setNationality(self, nationality):
        self.nationality = nationality

    def setAddress(self, address):
        self.address = address

    def setAge(self, age):
        if age < 0:
            raise ValueError("Age can't be negative number")
        self.age = age

    def printAll(self):
        print("\tCitizen:")
        print("FirstName : ",  self.firstName)
        print("SecondName : ", self.secondName)
        print("Ages : ", self.age)
        print("Nationality : ", self.nationality)
        print("Address : ", self.address)

