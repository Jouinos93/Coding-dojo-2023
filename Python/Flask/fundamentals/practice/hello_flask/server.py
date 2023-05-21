from flask import Flask
# Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
# Run the app in debug mode.

@app.route('/Dojo')
def Dojo():
    return 'Dojo'

@app.route('/say/<name>')
def say_name(name):
    if name == 'flask':
        return 'Hi Flask!'
    elif name == 'michael':
        return 'Hi Michael!'
    elif name == 'john':
        return 'Hi John!'
    else:
        return 'Unknown name'
@app.route('/repeat/<int:num>/<word>')
def repeat_word(num, word):
    result = word * num
    return result


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  