from flask import Blueprint

blueprint = Blueprint("calc", __name__)


@blueprint.route("/get-price", methods=("GET", ))
def get_price():
    return {}
