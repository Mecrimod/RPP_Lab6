import cherrypy
from model import Stan, InfStan

class MyApp(object):
    @cherrypy.expose
    def index(self):
        return f"""
        <html>
            <head>
                <title>Lab 6 web-разработка</title>
                <style>
                    table, th, td {{ border: 1px solid black; border-collapse: collapse; padding: 8px; }}
                    form {{ margin-top: 20px; }}
                </style>
            </head>
            <body>
                <h2>Osn Stan</h2>
                {self.table(Stan)}
                <h2>Stan Informations</h2>
                {self.table(InfStan)}
                <h2>Добавить Stan Information</h2>
                <form method="post" action="add">
                <label>Номер станка: <input type="text" name="number_stan"/></label><br/>
                <label>Модель: <input type="text" name="model"/></label><br/>
                <label>Дата покупки: <input type="text" name="date_buy"/></label><br/>
                <input type="submit" value="Добавить"/>
                 </form>
                <h2>Изменение Stan Informations</h2>
                <form method="post" action="update">
                    <label>Номер станка: <input type="text" name="number_stan"/></label><br/>
                    <label>Модель: <input type="text" name="model"/></label><br/>
                    <label>Дата покупки: <input type="text" name="date_buy"/></label><br/>
                    <input type="submit" value="Обновить"/>
                </form>
                <h2>Удалить Stan Information</h2>
                <form method="post" action="delete">
                <label>Номер станка: <input type="text" name="number_stan"/></label><br/>
                <input type="submit" value="Удалить"/>
            </form>
            </body>
        </html>
        """

    def table(self, model):
        html_table = "<table>"
        fields = model._meta.sorted_field_names
        html_table += "<tr>" + "".join(f"<th>{field}</th>" for field in fields) + "</tr>"
        for atr in model.select():
            row = "<tr>" + "".join(f"<td>{getattr(atr, field)}</td>" for field in fields) + "</tr>"
            html_table += row
        html_table += "</table>"
        return html_table

    @cherrypy.expose
    def add(self, number_stan, model, date_buy):
        try:
            number_stan = int(number_stan)
            InfStan.create(number_stan=number_stan, model=model, date_buy=date_buy)
            return f'<html><body>Запись добавлена. <a href="/">Вернуться на главную</a></body></html>'
        except Exception as e:
            return f'<html><body>Ошибка: {str(e)}. <a href="/">Вернуться на главную</a></body></html>'

    @cherrypy.expose
    def delete(self, number_stan):
        try:
            number_stan = int(number_stan)
            record = InfStan.get(InfStan.number_stan == number_stan)
            record.delete_instance()
            return f'<html><body>Запись удалена. <a href="/">Вернуться на главную</a></body></html>'
        except Exception as e:
            return f'<html><body>Ошибка: {str(e)}. <a href="/">Вернуться на главную</a></body></html>'

    @cherrypy.expose
    def update(self, number_stan, model, date_buy):
        try:
            number_stan = int(number_stan)
            record = InfStan.get(InfStan.number_stan == number_stan)
            record.model = model
            record.date_buy = date_buy
            record.save()
            return f'<html><body>Успешно обновлено. <a href="/">Вернуться на главную</a></body></html>'
        except Exception as e:
            return f'<html><body>Ошибка: {str(e)}. <a href="/">Вернуться на главную</a></body></html>'

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8080})
    cherrypy.quickstart(MyApp())
