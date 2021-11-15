from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome.."

@app.route("/helloworld")
def helloworld():
    user = request.args.get('user')
    if(user):
        return "Hello " + user
    return "Hello Stranger"

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8080"), debug=True)
