# create a flask app and run it
import json
from typing import Dict

from flask import Flask
from flask import Response
from flask import request
from http import HTTPStatus

from controller.account_manager import AccountManager

app = Flask(__name__)

accounts: AccountManager = AccountManager()


@app.route("/reset", methods=["POST"])
def reset():
    accounts.reset()
    return "<p>Reset</p>"


@app.route("/balance?account_id=<account_id>", methods=["GET"])
def balance(account_id):
    account = accounts.get_account(account_id)
    if account is None:
        return Response("0", status=HTTPStatus.NOT_FOUND)
    return Response(str(balance), status=HTTPStatus.OK)




@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
