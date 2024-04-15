import json

class ContactManager:
    def __init__(self):
        self.contact_list=[]
#add "self" for all of them
    def add(self,name,number):
        self.contact_list.append({"name":name,"number":number}) # use dictionary
        

    def search(self,name):
        result=[]
        for item in self.contact_list:
            if name.lower() in item["name"].lower():
                result.append(item)
        print(result)
    
    def backup(self):
        with open("./contact_list.json","w") as f:
            f.write(json.dumps(self.contact_list))      

    def print(self):
        print(f"your contact are:{self.contact_list}")

mycontact=ContactManager()
mycontact.add("fati","021")
mycontact.add("Fona","134")
mycontact.add("nada","213423")
mycontact.search("k")
mycontact.print()
mycontact.backup()