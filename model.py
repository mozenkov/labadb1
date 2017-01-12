import pickle

class Model:

    def __init__(self, file_name):
        self.contacts = []
        self.load(file_name)

    def load(self, file_name):
        try:
            with open(file_name, 'rb') as f:
                self.contacts = pickle.load(f)
        except:
            self.contacts = []

    def save(self, file_name):
        with open(file_name, 'wb') as f:
            pickle.dump([self.contacts], f)



    def add_contact(self, name, street):
        if  self.contacts == []:
            id = 0
        else:
            id = self.contacts[-1]['id']+1
        self.contacts.append({'id':id,'name':name,'street':street})