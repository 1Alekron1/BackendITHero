from flask import Blueprint, request, send_from_directory
from flask_jwt_extended import jwt_required, current_user
from flasgger import swag_from

from models import (
    session,
    User,
    Task,
    Recruit,
    Comment,
)
from swagger import (
    SWAGGER_ADD_COMMENT_TO_RECRUIT_STEP,
    SWAGGER_GET_RECRUITS_BY_TASK,
    SWAGGER_GET_TASKS_BY_HR,
    SWAGGER_GET_USER,
    SWAGGER_GET_SELF, GET_COMMENTS_BY_RECRUIT_STEP, GET_RECRUIT_FILE,
)

__all__ = ("common",)


common: Blueprint = Blueprint("common", __name__)


@common.route("/common/get_self", methods=["GET"])
@jwt_required()
@swag_from(SWAGGER_GET_SELF)
def get_self():
    return {
        "id": current_user.id,
        "firstName": current_user.first_name,
        "lastName": current_user.last_name,
    }, 200


@common.route("/common/get_user", methods=["GET"])
@jwt_required()
@swag_from(SWAGGER_GET_USER)
def get_user():
    try:
        user_id: int = int(request.args["userId"])
    except (KeyError, ValueError):
        return {"msg": "Invalid data"}, 400

    user: User | None = session.query(User).filter_by(id=user_id).first()
    if not user:
        return {"msg": "User not found"}, 404

    return {
        "id": user.id,
        "firstName": user.first_name,
        "lastName": user.last_name,
    }, 200


@common.route("/common/get_tasks_by_hr", methods=["GET"])
@jwt_required()
@swag_from(SWAGGER_GET_TASKS_BY_HR)
def get_tasks_by_hr():
    try:
        hr_id: int = int(request.args["hrId"])
    except (KeyError, ValueError):
        return {"msg": "Invalid data"}, 400

    tasks = []
    for task in session.query(Task).filter_by(hr_id=hr_id):
        tasks.append(
            {
                "id": task.id,
                "hrId": task.hr_id,
                "theme": task.theme,
                "description": task.description,
                "salaryRange": task.salary_range,
                "isCompleted": task.is_completed,
            }
        )

    return tasks, 200


@common.route("/common/get_recruits_by_task", methods=["GET"])
@jwt_required()
@swag_from(SWAGGER_GET_RECRUITS_BY_TASK)
def get_recruits_by_task():
    try:
        task_id: int = int(request.args["taskId"])
    except (KeyError, ValueError):
        return {"msg": "Invalid data"}, 400

    recruits = []
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


@common.route("/common/add_comment_to_recruit_step", methods=["POST"])
@jwt_required()
@swag_from(SWAGGER_ADD_COMMENT_TO_RECRUIT_STEP)
def add_comment_to_recruit_step():
    try:
        recruit_id: int = int(request.json["recruitId"])
        text: str = str(request.json["text"])
        step_num: int = int(request.json["stepNum"])
    except (KeyError, ValueError):
        return {"msg": "Invalid data"}, 400

    comment: Comment = Comment(
        recruit_id=recruit_id,
        text=text,
        step_num=step_num,
    )
    session.add(comment)
    session.commit()

    return {
        "id": comment.id,
        "recruitId": comment.recruit_id,
        "text": comment.text,
        "stepNum": comment.step_num,
    }, 201


@common.route('/common/get_comments_by_recruit_step', methods=['GET'])
@jwt_required()
@swag_from(GET_COMMENTS_BY_RECRUIT_STEP)
def get_comments_by_recruit_step():
    try:
        recruit_id: int = int(request.args['recruitId'])
        step_num: int = int(request.args['stepNum'])
    except (KeyError, ValueError):
        return {'msg': 'Invalid data'}, 400

    comments = []
    for comment in session.query(Comment).filter_by(
        recruit_id=recruit_id,
        step_num=step_num,
    ):
        comments.append({
            'id': comment.id,
            'recruitId': comment.recruit_id,
            'text': comment.text,
            'stepNum': comment.step_num,
        })

    return comments, 200




@common.route('/common/get_recruit_file', methods=['GET'])
@jwt_required()
@swag_from(GET_RECRUIT_FILE)
def get_recruit_file():
    try:
        recruit_id: int = int(request.args['recruitId'])
    except (KeyError, ValueError):
        return {'msg': 'Invalid data'}, 400

    path = './recruits/' + str(recruit_id)
    return send_from_directory('media', path)