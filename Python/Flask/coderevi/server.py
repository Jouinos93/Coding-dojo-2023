from flask import Flask, render_template,session,redirect,request
app = Flask(__name__)  
import random
app.secret_key='keep it secret..'

@app.route('/')
def index():          
    if "num" not in session:
        session ['num'] = random.randint()


if __name__=="__main__":  
    app.run(debug=True)