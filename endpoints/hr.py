import os
from typing import List

from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from werkzeug.datastructures import FileStorage

from config import UPLOAD_RECRUITS_FOLDER
from models import session, Recruit
from flasgger import swag_from

__all__ = ("hr",)

hr: Blueprint = Blueprint("hr", __name__)


@hr.route("/hr/upload_recruits", methods=["POST"])
<<<<<<< HEAD
@swag_from({
    'tags': ['HR'],
    'summary': 'Upload Recruits',
    'description': 'Endpoint to upload recruits.',
    'parameters': [
        {
            'name': 'taskId',
            'in': 'query',
            'type': 'integer',
            'required': True,
            'description': 'Task ID associated with recruits'
        }
    ],
    'responses': {
        200: {'description': 'Recruits uploaded successfully'},
        400: {'description': 'No file provided or invalid data'}
    }
})
=======
@jwt_required()
>>>>>>> bf8b1439cf1c9776b9a811e2e7157d75b0540df2
def upload_recruits():
    if not request.files:
        return {"msg": "No file"}, 400

    try:
        task_id: int = int(request.args['taskId'])
    except (KeyError, ValueError):
        return {'msg': 'Invalid data'}, 400

    for filename in request.files:
        file: FileStorage = request.files[filename]
        if file.filename.endswith(".pdf"):
            recruit: Recruit = Recruit(task_id=task_id)
            session.add(recruit)
            session.flush()

            file.save(os.path.join(UPLOAD_RECRUITS_FOLDER, str(recruit.id)))

    session.commit()

    recruits: List = []
    for recruit in session.query(Recruit).filter_by(task_id=task_id):
        recruits.append(
            {
                "id": recruit.id,
                "taskId": recruit.task_id,
                "stepNum": recruit.step_num,
                "gotOffer": recruit.got_offer,
            }
        )

    return recruits, 200


@hr.route("/hr/update_recruit_step", methods=["PUT"])
<<<<<<< HEAD
@swag_from({
    'tags': ['HR'],
    'summary': 'Update Recruit Step',
    'description': 'Endpoint to update recruit step.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'Recruit ID and new step number',
            'schema': {
                'type': 'object',
                'properties': {
                    'recruitId': {'type': 'integer'},
                    'stepNum': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Recruit step updated successfully'},
        400: {'description': 'No such recruit'}
    }
})
=======
@jwt_required()
>>>>>>> bf8b1439cf1c9776b9a811e2e7157d75b0540df2
def update_recruit_step():
    step_num: int = request.json.get("stepNum", None)
    recruit_id: int = request.json.get("recruitId", None)
    recruit: Recruit = session.query(Recruit).filter_by(id=recruit_id).first()
    if not recruit:
        return {"msg": "No such recruit"}, 400
    recruit.step_num = step_num
    session.add(recruit)
    session.commit()
