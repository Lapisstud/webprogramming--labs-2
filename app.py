from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return """
<!doctype html>
<html>
    <head>
        <title>Иванов Иван Иванович, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1 
        </header>
    
    <hl>web-сервер на flask</hl>

    <footer>
        &copу; Калинин Игорь, ФБИ-23, 3 курс, 2024
    </footer>
    </body>
</html>
"""