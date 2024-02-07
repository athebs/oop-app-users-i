class User:
    # intiate new clase with the users name, the username for the website, their 
    # email adddress and phone number 

    def __init__(self, name, user_name, email_address, phone_number) -> None:
        self._name = name 
        self._user_name = user_name
        self._email_address = email_address
        self._phone_number = phone_number

    def __str__(self) -> str:
        return f"This User is {self._name}, their User Name is {self._user_name}, email:{self._email_address}, phone_number:{self._phone_number} "
        

    
athena = User("Athena", "athebs", "athena@email.com", "123-456-7890")
tommy = User("tommy", "tommtomm", "tom@email.com", "999-999-9999")
print(athena)
print(tommy)