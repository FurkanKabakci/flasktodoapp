from flask import Flask,redirect,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/furka/Desktop/Python/TODOAPP/todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(80))
    complete= db.Column(db.Boolean)

@app.route("/")
def index():
    todos= Todo.query.all()
    return render_template("index.html",todos= todos)

@app.route("/add",methods=["post"])
def Addtodo():
    title=request.form.get("title")
    newTodo=Todo(title=title,complete=False)
    db.session.add(newTodo)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/complete/<string:id>")
def complete(id):
    todo= Todo.query.filter_by(id=id).first()
    todo.complete= not todo.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def delete(id):
    todo=Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))
    


if __name__=="__main__":
    with app.app_context():    
        db.create_all()
    app.run(debug=True)