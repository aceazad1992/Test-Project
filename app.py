from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return '''
    <html>
        <body>
            <form action = "/add" method = "POST">
                <input type = "text" name = "num1" /> +
                <input type = "text" name = "num2" />
                <input type = "submit" value = "Add" />
            </form>
        </body>
    </html>
    '''

@app.route('/add', methods=['POST'])
def add_two_nums():
    num1 = request.form['num1']
    num2 = request.form['num2']
    return str(int(num1) + int(num2))


if __name__ == '__main__':
    app.run()

app.run(port=5000, debug=True)
