# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

##############
#### HOME ####
##############

@app.route('/')
def home():
  return render_template('home.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)