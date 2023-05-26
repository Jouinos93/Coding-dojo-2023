from flask import Flask,render_template,session,redirect,request
app=Flask(__name__)
app.secret_key='keep it secret..'
@app.route('/')
def index():
    return render_template('index.html')




if __name__=="__name__":
    app.run (debug=True)