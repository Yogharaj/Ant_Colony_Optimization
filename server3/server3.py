from flask import Flask, request
app = Flask(__name__)
@app.route('/', methods=['POST'])
def calculate():
    n = int(request.form.get('n'))
    ans = 2 ** n
    return str(ans)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5002)

