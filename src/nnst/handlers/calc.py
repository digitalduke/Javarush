import json

from flask import (
    Blueprint,
    Response,
    request,
)
from nnst.db.db import DbManager


blueprint = Blueprint("calc", __name__)


@blueprint.route("/get-price", methods=("GET", ))
def get_price():
    raw_value = request.args.get('declared_cost')
    cargo_type = request.args.get('cargo_type').casefold()

    if not raw_value or not cargo_type:
        return Response(
            json.dumps({'error': 'Missing arguments'}),
            status=400,
            mimetype='application/json',
        )

    try:
        declared_cost = float(raw_value)
    except ValueError:
        return Response(
            json.dumps({'error': 'Invalid declared cost'}),
            status=400,
            mimetype='application/json',
        )

    rate = DbManager.get_current_rate_by_cargo_type(cargo_type)

    if not rate:
        return Response(
            json.dumps({'error': 'Unknown cargo type'}),
            status=400,
            mimetype='application/json',
        )

    insurance_cost = declared_cost * rate

    return Response(
        json.dumps({'insurance_cost': insurance_cost}),
        status=200,
        mimetype='application/json',
    )
