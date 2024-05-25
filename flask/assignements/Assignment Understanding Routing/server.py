from flask import Flask  # Import Flask to allow us to create our app
from werkzeug.exceptions import HTTPException

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def hello_dojo():
    return 'Dojo!'

@app.route('/say/<string:var>')
def hi_function(var):
    return f"Hi {var}!"

@app.route('/repeat/<int:num>/<string:var>')
def repeat_function(num, var):
    return f"{var * num}"

@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'Sorry! No response. Try again.'

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

