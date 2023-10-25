class Client:
    def __init__(self, first_name, last_name, address, cell_phone, email, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.cell_phone = cell_phone
        self.email = email
        self.gender = gender
    pass

client1 = Client('Cristiane', 'Pitana', 'Rua Santa fé, 92', '5199999999', 'cristianepitana@hotmail.com', 'f')
print(client1.first_name)


