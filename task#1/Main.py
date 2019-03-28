import Scientist as scientist


class Master(scientist.Scientist):
    def __init__(self):
        super().__init__()


class PhD(scientist.Scientist):
    def __init__(self):
        super().__init__()


class PhDoctor(scientist.Scientist):
    def __init__(self):
        super().__init__()


master = Master()
master.setFirstName("Dart")
master.setSecondName("Vader")
master.setAge(56)
master.setNationality("Tatuin")
master.setAddress("Death Star 2.0")
master.setCompanyAddress("Universe")
master.setCompanyName("Galactic Empire")
master.setArea(scientist.Area.Physics)
master.setType(scientist.Type.Experimenter)
master.setPapersNumber(504)
master.setPhoneNumber("8-800-504-42-42")

master.printAll()

phd = PhD()
phd.setFirstName("Frodo")
phd.setSecondName("Baggins")
phd.setAge(50)
phd.setNationality("Shire")
phd.setAddress("Shire, earthen mink")
phd.setCompanyAddress("MiddleEarth")
phd.setCompanyName("Fellowship of the ring")
phd.setArea(scientist.Area.Chemistry)
phd.setType(scientist.Type.Theorist)
phd.setPapersNumber(1)
phd.setPhoneNumber("8-800-101-41-67")

phd.printAll()

phDoctor = PhDoctor()

phDoctor = PhD()
phDoctor.setFirstName("Arthur")
phDoctor.setSecondName("Dent")
phDoctor.setAge(34)
phDoctor.setNationality("England")
phDoctor.setAddress("England")
phDoctor.setCompanyAddress("Universe")
phDoctor.setCompanyName("Hitchhiker")
phDoctor.setArea(scientist.Area.Mathematics)
phDoctor.setType(scientist.Type.Theorist)
phDoctor.setPapersNumber(42)
phDoctor.setPhoneNumber("0-000-101010")

phDoctor.printAll()