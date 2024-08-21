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


@app.route("/reset", methods=["GET", "POST"])
def reset():
    accounts.reset()
    return "OK", 200


@app.route("/balance", methods=["GET"])
def balance():
    account_id = request.args.get('account_id', default = '', type = str)
    account = accounts.get_account(account_id)
    if account is None:
        return Response("0", HTTPStatus.NOT_FOUND, mimetype='text/plain')
    return Response(str(account.get_balance()), mimetype='text/plain', status=HTTPStatus.OK)


@app.route("/event", methods=["POST"])
def event_handler():
    global accounts
    event = request.get_json()
    if event["type"] == "deposit":
        account = accounts.deposit(event["destination"], event["amount"])
        return Response(json.dumps({"destination": {"id": account.id, "balance": account.get_balance()}}),
                        status=HTTPStatus.CREATED)
    elif event["type"] == "withdraw":
        account = accounts.withdraw(event["origin"], event["amount"])
        if account is None:
            return Response("0", status=HTTPStatus.NOT_FOUND)
        return Response(json.dumps({"origin": {"id": account.id, "balance": account.get_balance()}}),
                        status=HTTPStatus.CREATED)
    elif event["type"] == "transfer":
        origin, destination = accounts.transfer(event["origin"], event["destination"], event["amount"])
        if origin is None:
            return Response("0", status=HTTPStatus.NOT_FOUND)
        return Response(json.dumps({"origin": {"id": origin.id, "balance": origin.get_balance()},
                                    "destination": {"id":destination.id, "balance": destination.get_balance()}}),
                        status=HTTPStatus.CREATED)
    else:
        return Response("0", status=HTTPStatus.BAD_REQUEST)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()