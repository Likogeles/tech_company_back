import sqlite3
from user import User


class UserList:

    _userList = []

    def __init__(self):
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        try:
            cur.execute("CREATE TABLE users(id, name, surname, email, password, department, isAdmin)")
        except Exception:
            pass

        result = list(cur.execute("SELECT * FROM users;").fetchall())

        for i in result:
            self._userList.append(User(int(i[0]), i[1], i[2], i[3], i[4], i[5], i[6]))

        con.close()

    def addUser(self, new_user):
        self._userList.append(new_user)
        con = sqlite3.connect("users.db")
        cur = con.cursor()

        cur.execute(f"""INSERT INTO users VALUES('{new_user.id}', '{new_user.name}', '{new_user.surname}', '{new_user.email}', '{new_user.password}', '{new_user.department}', '{new_user.isAdmin}')""")
        con.commit()
        con.close()
        
    def updateUser(self, new_user):
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute(
            f"UPDATE users SET id = '{new_user.id}', name = '{new_user.name}', surname = '{new_user.surname}', email = '{new_user.email}', password = '{new_user.password}' , department = '{new_user.department}' , isAdmin = '{new_user.isAdmin}' WHERE id = '{new_user.id}';")
        con.commit()
        
        self._userList.clear()
        result = list(cur.execute("SELECT * FROM users;").fetchall())
        for i in result:
            self._userList.append(User(int(i[0]), i[1], i[2], i[3], i[4], i[5], i[6]))
        con.close()

    def removeUser(self, id):
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute(
            f"DELETE FROM users WHERE id = '{id}';")
        con.commit()
        
        self._userList.clear()
        result = list(cur.execute("SELECT * FROM users;").fetchall())
        for i in result:
            self._userList.append(User(int(i[0]), i[1], i[2], i[3], i[4], i[5], i[6]))
        con.close()
    
    def getUser(self) -> list[User]:
        return self._userList

    def __str__(self):
        usersStr = ""
        for i in self._userList:
            usersStr += f"{i.id}: {i.name} {i.surname} {i.email} {i.department}\n"
        return usersStr

    def to_json(self):
        usersJson = {'users': []}
        for i in self._userList:
            usersJson['users'].append({'id': i.id, 'name': i.name, 'surname': i.surname, 'email': i.email, 'password': i.password, 'department': i.department, 'isAdmin': i.isAdmin})
        return usersJson
