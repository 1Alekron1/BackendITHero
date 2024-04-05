from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from models import (
    User,
    Task,
    session,
)

__all__ = (
    'boss',
)

# FixMe: функциями руководителя может пользоваться и hr (проверки пока нет)
boss: Blueprint = Blueprint('boss', __name__)


@boss.route('/boss/register_hr', methods=['POST'])
@jwt_required()
def register_hr():
    try:
        first_name: str = str(request.json['firstName'])
        last_name: str = str(request.json['lastName'])
        username: str = str(request.json['username'])
        password: str = str(request.json['password'])
    except KeyError:
        return {'msg': 'Invalid data'}, 400

    hr: User = User(
        first_name=first_name,
        last_name=last_name,
        username=username,
        password=password,
        is_hr=True,
    )
    session.add(hr)
    session.commit()

    return {'msg': 'HR was created'}, 201


@boss.route('/boss/get_hrs', methods=['GET'])
@jwt_required()
def get_hrs():
    hrs = []
    for hr in session.query(User).filter_by(is_hr=True):
        hrs.append({
            'id': hr.id,
            'firstName': hr.first_name,
            'lastName': hr.last_name,
        })

    return hrs


@boss.route('/boss/create_task', methods=['POST'])
def create_task():
    pass


@boss.route('/boss/set_task_to_hr', methods=['PUT'])
def set_task_to_hr():
    pass


@boss.route('/boss/set_task_as_completed', methods=['PUT'])
def set_task_as_completed():
    pass


@boss.route('/boss/set_offer_to_recruit', methods=['PUT'])
def set_offer_to_recruit():
    pass
