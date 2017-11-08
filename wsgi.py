from flask import Flask
import requests

application = Flask(__name__)

@application.route("/")
def hello():
    print "dispatching request"
    r = requests.get('http://ocfirst/')
    print r.text
    return r.text

if __name__ == "__main__":
    application.run()
