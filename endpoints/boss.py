from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from models import (
    User,
    Task,
    Recruit,
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

    return {
        'id': hr.id,
        'firstName': hr.first_name,
        'lastName': hr.last_name,
    }, 201


@boss.route('/boss/get_hrs', methods=['GET'])
@jwt_required()
def get_hrs():
    hrs = []
    for hr in session.query(User).filter_by(is_hr=True).all():
        hrs.append({
            'id': hr.id,
            'firstName': hr.first_name,
            'lastName': hr.last_name,
        })

    return hrs, 200


@boss.route('/boss/create_task', methods=['POST'])
@jwt_required()
def create_task():
    hr_id: int | None
    try:
        hr_id = int(request.json['hrId'])
    except (KeyError, ValueError):
        hr_id = None

    try:
        theme: str = str(request.json['theme'])
        description: str = str(request.json['description'])
        salary_range: str = str(request.json['salaryRange'])
    except (KeyError, ValueError):
        return {'msg': 'Invalid data'}, 400

    task: Task = Task(
        hr_id=hr_id,
        theme=theme,
        description=description,
        salary_range=salary_range,
    )
    session.add(task)
    session.commit()

    return {
        'id': task.id,
        'hrId': task.hr_id,
        'theme': task.theme,
        'description': task.description,
        'salaryRange': task.salary_range,
    }, 201


@boss.route('/boss/set_task_to_hr', methods=['PUT'])
@jwt_required()
def set_task_to_hr():
    try:
        task_id: int = int(request.json['taskId'])
        hr_id: int = int(request.json['hrId'])
    except (KeyError, ValueError):
        return {'msg': 'Invalid data'}, 400

    task: Task | None = session.query(Task).filter_by(
        id=task_id,
    ).first()
    if not task:
        return {'msg': 'Task not found'}, 404

    task.hr_id = hr_id
    session.commit()

    return {'msg': 'Operation is completed'}, 200


@boss.route('/boss/set_task_as_completed', methods=['PUT'])
@jwt_required()
def set_task_as_completed():
    try:
        task_id: int = int(request.json['taskId'])
    except (KeyError, ValueError):
        return {'msg': 'Invalid data'}, 400

    task: Task | None = session.query(Task).filter_by(
        id=task_id,
    ).first()
    if not task:
        return {'msg': 'Task not found'}, 404

    task.is_completed = True
    session.commit()

    return {'msg': 'Operation is completed'}, 200


@boss.route('/boss/set_offer_to_recruit', methods=['PUT'])
@jwt_required()
def set_offer_to_recruit():
    try:
        recruit_id: int = int(request.json['recruitId'])
    except (KeyError, ValueError):
        return {'msg': 'Invalid data'}, 400

    recruit: Recruit | None = session.query(Recruit).filter_by(
        id=recruit_id,
    ).first()
    if not recruit:
        return {'msg': 'Recruit not found'}, 404

    recruit.got_offer = True
    session.commit()

    return {'msg': 'Operation is completed'}, 200
