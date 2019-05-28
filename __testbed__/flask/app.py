from flask import Flask


app = Flask(__name__)

@app.route('/<string:message>', methods=['GET', 'POST'])
def hello(message):
    return f"""<html>
        <head>
            <link rel="stylesheet" type="text/css" href="static/main.css">
        </head>
        <body>
            <b>Hello {message}</b>
        </body>
    </html>"""