from flask import Flask,redirect,request,url_for,render_template,request
app = Flask(__name__)

@app.route('/login',methods = ['POST'])
def login():
    username="Juliukinns"
    password="1234"
    if request.form["username"] != username:
        return render_template("error.html", msg="Invalid user")
    if request.form["password"] != password:
        return render_template("error.html", msg="Invalid Password")

    return render_template("welcome.html", username=username )

     
        
  
if __name__ == '__main__':
   app.run(debug = True)