from flask import Flask, render_template
app=Flask (__name__)

@app.route('/play/<int:number>')
def box(number):
    return render_template("play.html",number=number)
@app.route('/test/<int:num>')
def tester(num):
    return render_template("test.html",num=num)


if __name__=="__main__":
    app.run(debug=True) 
