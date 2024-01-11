from flask import Flask, request
from tech import Tech

from techs import TechList

app = Flask(__name__)

techList = TechList()

techList.addTech(Tech("1", "Принтер", "Охрана", "Работает", "Общее"))
techList.addTech(Tech("2", "Компьютер 1", "Отдел продаж", "Работает", "Личное"))
techList.addTech(Tech("3", "Ксерокс", "Отдел кадров", "Требуется ремонт", "Общее"))
techList.addTech(Tech("4", "Куллер", "Отдел продаж", "В ремонте", "Общее"))
techList.addTech(Tech("5", "Кофемашина", "Технический отдел", "Неисправно", "Общее"))

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

@app.route('/techs')
def techs():
    return techList.to_json()

@app.route('/')
def hello():
    return f'Сервер работает'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
