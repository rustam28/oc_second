from flask import Flask
import requests
import os

application = Flask(__name__)

@application.route("/")
def hello():
    ocfirst_host = os.environ['OCFIRST_SERVICE_HOST']
    ocfirst_port = os.environ['OCFIRST_SERVICE_PORT']
    url = 'https://%s:%s/' % (ocfirst_host, ocfirst_port)
    print 'dispatching request to %s' % url
    r = requests.get('http://ocfirst/')
    print r.text
    return r.text

if __name__ == "__main__":
    application.run()
