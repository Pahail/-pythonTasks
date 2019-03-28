import Citizen as citizen


class Worker(citizen.Citizen):

    def __init__(self):
        super().__init__()
        self.companyName = ""
        self.companyAddress = ""
        self.phoneNumber = ""

    def getCompanyName(self):
        return self.companyName

    def getCompanyAddress(self):
        return self.companyAddress

    def getPhoneNumber(self):
        return self.phoneNumber

    def setCompanyName(self, company_name):
        self.companyName = company_name

    def setCompanyAddress(self, address):
        self.companyAddress = address

    def setPhoneNumber(self, phone):
        self.phoneNumber = phone

    def printAll(self):
        super().printAll()
        print("\tWorker:")
        print("Company name : ", self.companyName)
        print("Company address :", self.companyAddress)
        print("Phone number :", self.phoneNumber)
