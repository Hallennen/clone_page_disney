from flask import Flask , render_template

page = Flask(__name__)

@page.route("/")
def teste():
    return render_template('disney.html')


page.run(host='localhost',port=5000 , debug=True)
