import sqlite3
from tech import Tech


class TechList:

    _techList = []

    def __init__(self):
        con = sqlite3.connect("techs.db")
        cur = con.cursor()
        try:
            cur.execute("CREATE TABLE techs(id, name, category, tech_state, department)")
        except Exception:
            pass

        result = list(cur.execute("SELECT * FROM techs;").fetchall())

        for i in result:
            self._techList.append(Tech(int(i[0]), i[1], i[2], i[3], i[4]))

        con.close()

    def addTech(self, new_tech):
        self._techList.append(new_tech)
        con = sqlite3.connect("techs.db")
        cur = con.cursor()

        cur.execute(f"""INSERT INTO techs VALUES('{new_tech.id}', '{new_tech.name}', '{new_tech.category}', '{new_tech.tech_state}', '{new_tech.department}')""")
        con.commit()
        con.close()
        
    def updateTech(self, new_tech):
        con = sqlite3.connect("techs.db")
        cur = con.cursor()
        cur.execute(
            f"UPDATE techs SET id = '{new_tech.id}', name = '{new_tech.name}', category = '{new_tech.category}', tech_state = '{new_tech.tech_state}', department = '{new_tech.department}' WHERE id = '{new_tech.id}';")
        con.commit()
        
        self._techList.clear()
        result = list(cur.execute("SELECT * FROM techs;").fetchall())
        for i in result:
            self._techList.append(Tech(int(i[0]), i[1], i[2], i[3], i[4]))
        con.close()

    def removeTech(self, id):
        con = sqlite3.connect("techs.db")
        cur = con.cursor()
        # DELETE FROM table_name WHERE condition
        cur.execute(
            f"DELETE FROM techs WHERE id = '{id}';")
        con.commit()
        
        self._techList.clear()
        result = list(cur.execute("SELECT * FROM techs;").fetchall())
        for i in result:
            self._techList.append(Tech(int(i[0]), i[1], i[2], i[3], i[4]))
        con.close()
    
    def getTech(self) -> list[Tech]:
        return self._techList

    def __str__(self):
        techsStr = ""
        for i in self._techList:
            techsStr += f"{i.id}: {i.name} {i.category} {i.tech_state} {i.department}\n"
        return techsStr

    def to_json(self):
        techsJson = {'techs': []}
        for i in self._techList:
            techsJson['techs'].append({'id': i.id, 'name': i.name, 'category': i.category, 'tech_state': i.tech_state, 'department': i.department})
        return techsJson
