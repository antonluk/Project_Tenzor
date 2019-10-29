import os
from flask import Flask, request, jsonify, json, redirect, render_template
from jinja2 import Environment, PackageLoader, select_autoescape
from flask_sqlalchemy import SQLAlchemy
from app.models import Client
# from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

project_dir = os.path.dirname(os.path.abspath(__file__))

database_file = "sqlite:///{}".format(os.path.join(project_dir + "/app/db/", "test.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

env = Environment(loader=PackageLoader('app', 'templates'), autoescape=select_autoescape(['html', 'xml']))
app = Flask(__name__, template_folder='app/templates')


# TODO: перенести в app/db
class Client(db.Model):
    client_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    nick_name = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    middle_name = db.Column(db.String)
    gender = db.Column(db.Integer)
    birth_date = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    city_id = db.Column(db.Integer, nullable=False)
    district_id = db.Column(db.Integer, nullable=False)

    # def __repr__(self):
    #     return self


db.create_all()


# TODO: методы перенести в модули
@app.route('/', methods=['GET'])
def home():
    title = 'Секретный проект'
    return render_template("index.html", name=title)


@app.route('/api/client', methods=['GET'])
@app.route('/api/clients', methods=['GET'])
def clients_list():
    if request.form:
        client = Client(nick_name=request.form.get("client_id"))
        db.session.add(client)
        db.session.commit()

    clients = Client.query.all()
    # return jsonify(clients)
    return render_template("clients.html", clients=clients)


@app.route('/api/client/new', methods=['POST'])
def client_new():
    if request.method == 'POST':
        new_client = Client(
            nick_name=request.form['nick_name'],
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            middle_name=request.form['middle_name'],
            gender=request.form['gender'],
            birth_date=request.form['birth_date'],
            email=request.form['email'],
            phone=request.form['phone'],
            address=request.form['address'],
            city_id=request.form['city_id'],
            district_id=request.form['district_id']
        )
        db.session.add(new_client)
        db.session.commit()
        db.session.close()
        return redirect('/')


@app.route('/api/client/<int:client_id>', methods=['PUT'])
def client_update(client_id):
    update_client = db.session.query(Client).filter_by(client_id=client_id).one()
    if 'nick_name' in request.form:
        update_client.nick_name = request.form['nick_name']
    if 'first_name' in request.form:
        update_client.first_name = request.form['first_name']
    if 'last_name' in request.form:
        update_client.last_name = request.form['last_name']
    if 'middle_name' in request.form:
        update_client.middle_name = request.form['middle_name']
    if 'gender' in request.form:
        update_client.gender = request.form['gender']
    if 'birth_date' in request.form:
        update_client.birth_date = request.form['birth_date']
    if 'email' in request.form:
        update_client.email = request.form['email']
    if 'phone' in request.form:
        update_client.phone = request.form['phone']
    if 'address' in request.form:
        update_client.address = request.form['address']
    if 'city_id' in request.form:
        update_client.city_id = request.form['city_id']
    if 'district_id' in request.form:
        update_client.district_id = request.form['district_id']
    return redirect('/')


@app.route('/api/client/<int:client_id>', methods=['DELETE'])
def client_delete(client_id):
    delete_client = db.session.query(Client).filter_by(client_id=client_id).one()
    db.session.delete(delete_client)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)
