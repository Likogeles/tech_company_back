from flask import Flask, request
from tech import Tech

from techs import TechList
from user import User
from users import UserList

app = Flask(__name__)

techList = TechList()
userList = UserList()

# techList.addTech(Tech("1", "Принтер",  "Общее", "Работает","Охрана"))
# techList.addTech(Tech("2", "Компьютер 1",  "Личное", "Работает","Отдел продаж"))
# techList.addTech(Tech("3", "Ксерокс",  "Общее", "Требуется ремонт","Отдел кадров"))
# techList.addTech(Tech("4", "Куллер",  "Общее", "В ремонте", "Отдел продаж"))
# techList.addTech(Tech("5", "Кофемашина",  "Общее", "Неисправно","Технический отдел"))

# userList.addUser(User("1", "Иван", "Сидоров", "ivan@ya.ru", "qwerty1234", "Охрана", "1"))
# userList.addUser(User("2", "Федор", "Иванов", "fedor@ya.ru", "qwerty1234", "Отдел продаж", "1"))
# userList.addUser(User("3", "Сергей", "Петров", "sergey@ya.ru", "qwerty1234", "Технический отдел", "0"))
# userList.addUser(User("4", "Петр", "Сергеев", "petr@ya.ru", "qwerty1234", "Отдел кадров", "0"))
# userList.addUser(User("5", "Владимир", "Маяковский", "vladimir@ya.ru", "qwerty1234", "Охрана", "0"))

@app.route('/add_tech')
def add_tech():
    id = request.args.get('id')
    name = request.args.get('name')
    category = request.args.get('category')
    tech_state = request.args.get('tech_state')
    department = request.args.get('department')
    if id != None and name != None and category != None and tech_state != None and department != None:
        techList.addTech(Tech(id, name, category, tech_state, department))
        return "Успешно"
    else:
        return "Неудача"
    
@app.route('/update_tech')
def update_tech():
    id = request.args.get('id')
    name = request.args.get('name')
    category = request.args.get('category')
    tech_state = request.args.get('tech_state')
    department = request.args.get('department')
    if id != None and name != None and category != None and tech_state != None and department != None:
        techList.updateTech(Tech(id, name, category, tech_state, department))
        return "Успешно"
    else:
        return "Неудача"
    
@app.route('/remove_tech')
def remove_tech():
    id = request.args.get('id')
    if id != None:
        techList.removeTech(id)
        return "Успешно"
    else:
        return "Неудача"

@app.route('/techs')
def techs():
    return techList.to_json()


@app.route('/add_user')
def add_user():
    id = request.args.get('id')
    name = request.args.get('name')
    surname = request.args.get('surname')
    email = request.args.get('email')
    password = request.args.get('password')
    department = request.args.get('department')
    isAdmin = request.args.get('isAdmin')
    if id != None and name != None and surname != None and email != None and password != None and department != None and isAdmin != None:
        userList.addTech(Tech(id, name, surname, email, password, department, isAdmin))
        return "Успешно"
    else:
        return "Неудача"
    
@app.route('/update_user')
def update_user():
    id = request.args.get('id')
    name = request.args.get('name')
    surname = request.args.get('surname')
    email = request.args.get('email')
    password = request.args.get('password')
    department = request.args.get('department')
    isAdmin = request.args.get('isAdmin')
    if id != None and name != None and surname != None and email != None and password != None and department != None and isAdmin != None:
        userList.addTech(Tech(id, name, surname, email, password, department, isAdmin))
        return "Успешно"
    else:
        return "Неудача"
    
@app.route('/remove_user')
def remove_user():
    id = request.args.get('id')
    if id != None:
        userList.removeuser(id)
        return "Успешно"
    else:
        return "Неудача"

@app.route('/users')
def users():
    return userList.to_json()


@app.route('/')
def hello():
    return f'Сервер работает'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
