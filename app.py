from flask import Flask , redirect, url_for, render_template, request ,jsonify
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
import json




app = Flask(__name__,template_folder="templates",static_folder="static")
app.config["SECRET_KEY"] = "lechiduy2002"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/qlnv'
db = SQLAlchemy(app)


class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    id_employee = db.Column(db.String(20), nullable=False)
    name_employee = db.Column(db.String(50), nullable=False)
    group_employee = db.Column(db.String(20), nullable=False)
    start_date = db.Column(db.String(20), nullable=False)
    training_date = db.Column(db.String(20), nullable=False)
    trainer = db.Column(db.String(50), nullable=False)
    training_stage = db.Column(db.String(500), nullable=False)
    comments = db.Column(db.String(500), nullable=False)
    notes = db.Column(db.String(500), nullable=False)

@app.route("/")
def home():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="qlnv"
)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee ORDER BY id")
    rows = cursor.fetchall()

    row_number = 1
    for row in rows:
        cursor.execute("UPDATE employee SET id = %s WHERE id = %s", (row_number, row[0]))
        row_number += 1

    conn.commit()

    cursor.close()
    conn.close()
    data = Employee.query.all()
    return render_template("home.html" , data=data) 

@app.route("/create", methods = ['POST','GET'])
def create():
    if request.method == "POST":
        id_employee = request.form.get("Id_Employee")
        name_employee = request.form.get("nameEmployee")
        group_employee = request.form.get("groupEmployee")
        start_date = request.form.get("startDate")
        training_date = request.form.get("trainingDate")
        trainer = request.form.get("trainer")
        training_stage = request.form.get("trainingStage")
        comments = request.form.get("comments")
        notes = request.form.get("notes")

        new_employee = Employee(id_employee = id_employee,
                               name_employee = name_employee,
                               group_employee = group_employee,
                               start_date = start_date,
                               training_date = training_date,
                               trainer = trainer,
                               training_stage = training_stage,
                               comments = comments,
                               notes = notes)
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("create.html")

@app.route("/delete", methods=["POST","GET"])
def delete():
    employee = json.loads(request.data)
    employee_id = employee["employee_id"]
    result = Employee.query.get(employee_id)
    if result:
        db.session.delete(result)
        db.session.commit()
    return jsonify({'code' : 200})

@app.route("/employee/<int:id>", methods = ["GET","POST"])
def get_by_id(id):
    employee = Employee.query.get(id)
    if request.method == "POST":
        employee.id_employee = request.form.get("Id_Employee")
        employee.name_employee = request.form.get("nameEmployee")
        employee.group_employee = request.form.get("groupEmployee")
        employee.start_date = request.form.get("startDate")
        employee.training_date = request.form.get("trainingDate")
        employee.trainer = request.form.get("trainer")
        employee.training_stage = request.form.get("trainingStage")
        employee.comments = request.form.get("comments")
        employee.notes = request.form.get("notes")

        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html",employee = employee)
    
    
@app.route("/employee/<int:id>", methods = ["GET"])
def edit_by_id(id):
    employee = Employee.query.get(id)
    id_employee = request.form.get("Id_Employee")
    name_employee = request.form.get("nameEmployee")
    group_employee = request.form.get("groupEmployee")
    start_date = request.form.get("startDate")
    training_date = request.form.get("trainingDate")
    trainer = request.form.get("trainer")
    training_stage = request.form.get("trainingStage")
    comments = request.form.get("comments")
    notes = request.form.get("notes")
    if employee:
        employee = Employee(id_employee = id_employee,
                               name_employee = name_employee,
                               group_employee = group_employee,
                               start_date = start_date,
                               training_date = training_date,
                               trainer = trainer,
                               training_stage = training_stage,
                               comments = comments,
                               notes = notes)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html")
    
@app.route("/search", methods = ["POST"])
def searching():
    if request.method == "POST":
        print(request.form.get('key_word')) 
        query = request.form.get('key_word')
        results = db.session.query(Employee).filter(Employee.name_employee.ilike(f'%{query}%')).all()
        print(results)
        return render_template('search_result.html',query = query,  results = results)
    

if __name__ == "__main__":
    app.run(debug=True)