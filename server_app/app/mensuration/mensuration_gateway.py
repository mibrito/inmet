from app import session
from flask import Blueprint
from flask import Response
import json
from app.mensuration.mensuration_controller import MensurationController


mensuration = Blueprint('mensuration', __name__, url_prefix='/mensuration')


@mensuration.route('/getFrequencyPerMonth', methods=['GET'])
def getFrequencyPerYear():
    mensurationController = MensurationController()
    response = mensurationController.getFrequencyPerYear()

    return Response(json.dumps(response), mimetype='application/json')

