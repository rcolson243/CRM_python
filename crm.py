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
    
if __name__ == "__main__":
    from faker import Faker
    fake = Faker(locale="fr_FR")
    for _ in range(10):
        new_user = User(fake.first_name(),fake.last_name(),fake.phone_number(),fake.address())
        print(new_user)
        print("-" *10)
        print(new_user.__repr__())
