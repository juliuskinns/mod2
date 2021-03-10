from flask import Flask,render_template

app=Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def index():
   return render_template("login.html")

@app.route('/students',methods = ['GET', 'POST'])
def student():
   student=["James","John","Joan"]
   return render_template("students.html",students=student)

if __name__ == '__main__':
   app.run()