from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return """
<!doctype html>
<html>
    <head>
        <title>Иванов Иван Иванович, лабораторная 1</title>
    </head>
    <body>
        <header>
           НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
    
    <hl></hl>

    <footer>
        &copу; Калинин Игорь, ФБИ-23, 3 курс, 2024
    </footer>
    </body>
</html>
"""
@app.route("/lab1")
def lab1():
    return"""
<!doctype html>
<html>
    <head>
        <title>Иванов Иван Иванович, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1 
        </header>
    
    <hl>Flask — фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков — минималистичных каркасов веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</hl>

    <footer>
        &copу; Калинин Игорь, ФБИ-23, 3 курс, 2024
    </footer>
    </body>
</html>
"""