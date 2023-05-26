from flask import Flask ,render_template   
# Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def play():
    return render_template('play.html')  # Return the string 'Hello World!' as a response


@app.route('/play/<int:nums>/<string:color>')
def index(nums, color):
    return render_template('play.html' , num=nums, color=color)

if __name__=="__name__":
    app.run (debug=True)
