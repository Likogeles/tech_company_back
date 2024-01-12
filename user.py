class User:
    id = "-1"
    name = "-1"
    surname = "-1"
    email = "-1"
    password = "-1"
    department = "-1"
    isAdmin = "-1"

    def __init__(self, id, name, surname, email, password, department, isAdmin):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.department = department
        self.isAdmin = isAdmin
