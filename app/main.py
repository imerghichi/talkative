from flask import Flask

app = Flask(__name__, template_folder='templates')
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/deliverActCode', methods=['POST'])
def deliverActCode():
    return "test"
