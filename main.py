import cherrypy
from model import Stan, inf_stan

class MyApp(object):
    @cherrypy.expose
    def index(self):
        return f"""
        <html>
            <head>
                <title>Lab 6 web-разработка</title>
                <style>
                   table, th, td {{ border: 1px solid black; border-collapse: collapse; padding: 8px; }}
                </style>
            </head>
            <body>
                <h2>Osn Stan</h2>
                {self.table(Stan)}
                <h2>Stan Informations</h2>
                {self.table(inf_stan)}
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

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8080})
    cherrypy.quickstart(MyApp())
