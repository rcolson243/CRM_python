import re
import string
class User:
    def __init__(self, first_name:str, last_name:str, phone_number:str, address:str):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
    
    def __repr__(self):
        return f"User({self.first_name},{self.last_name})"
    
    def __str__(self):
        return(f"""
            {self.Full_name}
            {self.phone_number}
            {self.address}
    """)
    @property 
    def Full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def check_phone_number(self):
        phone_digits = re.sub(r"[+()\s]*", "", self.phone_number)
        if len(phone_digits) < 10 or not phone_digits.isdigit():
            raise ValueError(f"Numéro de téléphone {self.phone_number} invalide")
        
    def check_names(self):
        if not (self.first_name and self.last_name):
            raise ValueError("Veiller bien rentrer vos information")
        
        special_characters = string.punctuation + string.digits
        # print(special_characters)

        for characters in self.Full_name:
            if characters in special_characters:
                raise ValueError(f"Non invalide{self.Full_name}.")
            
    def check_all(self):
        self.check_names()
        self.check_phone_number()

if __name__ == "__main__":
    from faker import Faker
    fake = Faker(locale="fr_FR")
    for _ in range(10):
        new_user = User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone_number = fake.phone_number(),
            address =fake.address()
        )
        print(new_user)
        new_user.check_all()
        print("-" *10)
