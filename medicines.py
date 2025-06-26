print("And if I am ill, He heals me.\n")

disease_name = input("Write your disease name:")
symptoms= input("Write symptoms of this disease:").split()

class Disease:
    def __init__(self,name ,symptoms):
        self.name=name
        self.symptoms=symptoms


    def display(self):
        return f"You have a {self.name} and its symptoms is {self.symptoms}"

class Disease_Directory:
    def __init__(self):
        self.disease_name=[]

    def add_disease(self,disease):
        self.disease_name.append(disease)

    def search_by_symptom(self,symptom):
        found = False

        for disease in self.disease_name:
            if symptom in disease.symptoms:
                print(disease.display())
                found = True
            else:
                print("We haven't found the symptom")

d1 = Disease(disease_name, symptoms)
directory = Disease_Directory()
directory.add_disease(d1)

symptoms_to_search = input("Write your symptoms:")
directory.search_by_symptom(symptoms_to_search)


