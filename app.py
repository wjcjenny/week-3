from flask import Flask
from flask import render_template
import json
import time

# we are not importing the whole library but only the two Classes that we need from it. 

# create a variable to store an instance of the Flask class:
app = Flask(__name__)
#Using this variable we can access the server and specify how the server should handle incoming requests.

# create one route, which will handle requests coming into the main path of the server.
@app.route("/")
# execute every time a request is sent to this route, and whatever is returned from the function will be sent back to the user making the request. 
def index():
    return render_template("index.html")


@app.route("/getData/")
def getData():
    print "getting the data"
    output = {"out":time.strftime('%X %x %Z')}
    return json.dumps(output)

# start the server on a specific local path
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True,threaded=True)



