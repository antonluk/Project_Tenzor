from flask import Flask, request, jsonify
from jinja2 import Environment, PackageLoader, select_autoescape

from app.models import Client

env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

app = Flask(__name__)


@app.route('/')
def __init__():
    template = env.get_template('index.html')
    return template.render(name='Тут будет какой-то очень классный проект')


@app.route('/api/get_user/<uuid>', methods=['GET'])
def get_user(uuid):
    return jsonify(
        {"uuid": uuid},
        {"client": Client.Client.get_client_mock()}
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
