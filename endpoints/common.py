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

__all__ = (
    'common',
)

common: Blueprint = Blueprint('common', __name__)


@common.route('/common/get_self', methods=['GET'])
@jwt_required()
@swag_from({
    'tags': ['Common'],
    'summary': 'Get Self',
    'description': 'Endpoint to get information about the current user.',
    'responses': {
        200: {'description': 'Information about the current user'},
    }
})
def get_self():
    return {
        'id': current_user.id,
        'firstName': current_user.first_name,
        'lastName': current_user.last_name,
    }, 200


@common.route('/common/get_user', methods=['GET'])
@jwt_required()
@swag_from({
    'tags': ['Common'],
    'summary': 'Get User',
    'description': 'Endpoint to get information about a specific user.',
    'parameters': [
        {
            'name': 'userId',
            'in': 'query',
            'type': 'integer',
            'required': True,
            'description': 'ID of the user to retrieve information about.'
        }
    ],
    'responses': {
        200: {'description': 'Information about the requested user'},
        404: {'description': 'User not found'},
    }
})
def get_user():
    try:
        user_id: int = int(request.args['userId'])
    except (KeyError, ValueError):
        return {'msg': 'Invalid data'}, 400

    user: User | None = session.query(User).filter_by(id=user_id).first()
    if not user:
        return {'msg': 'User not found'}, 404

    return {
        'id': user.id,
        'firstName': user.first_name,
        'lastName': user.last_name,
    }, 200


@common.route('/common/get_tasks_by_hr', methods=['GET'])
@jwt_required()
@swag_from({
    'tags': ['Common'],
    'summary': 'Get Tasks by HR',
    'description': 'Endpoint to get tasks assigned to a HR user.',
    'parameters': [
        {
            'name': 'hrId',
            'in': 'query',
            'type': 'integer',
            'required': True,
            'description': 'ID of the HR user to fetch tasks for.'
        }
    ],
    'responses': {
        200: {'description': 'List of tasks assigned to the HR user'},
    }
})
def get_tasks_by_hr():
    try:
        hr_id: int = int(request.args['hrId'])
    except (KeyError, ValueError):
        return {'msg': 'Invalid data'}, 400

    tasks = []
    for task in session.query(Task).filter_by(hr_id=hr_id):
        tasks.append({
            'id': task.id,
            'hrId': task.hr_id,
            'theme': task.theme,
            'description': task.description,
            'salaryRange': task.salary_range,
            'isCompleted': task.is_completed,
        })

    return tasks, 200


@common.route('/common/get_recruits_by_task', methods=['GET'])
@jwt_required()
@swag_from({
    'tags': ['Common'],
    'summary': 'Get Recruits by Task',
    'description': 'Endpoint to get recruits associated with a task.',
    'parameters': [
        {
            'name': 'taskId',
            'in': 'query',
            'type': 'integer',
            'required': True,
            'description': 'ID of the task to fetch recruits for.'
        }
    ],
    'responses': {
        200: {'description': 'List of recruits associated with the task'},
    }
})
def get_recruits_by_task():
    try:
        task_id: int = int(request.args['taskId'])
    except (KeyError, ValueError):
        return {'msg': 'Invalid data'}, 400

    recruits = []
    for recruit in session.query(Recruit).filter_by(task_id=task_id):
        recruits.append({
            'id': recruit.id,
            'taskId': recruit.task_id,
            'stepNum': recruit.step_num,
            'gotOffer': recruit.got_offer,
        })

    return recruits, 200


@common.route('/common/add_comment_to_recruit_step', methods=['POST'])
@jwt_required()
@swag_from({
    'tags': ['Common'],
    'summary': 'Add Comment to Recruit Step',
    'description': 'Endpoint to add a comment to a recruit\'s step.',
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
                    'text': {'type': 'string'},
                    'stepNum': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        201: {'description': 'Comment added successfully'},
        400: {'description': 'Invalid data provided'},
    }
})
def add_comment_to_recruit_step():
    try:
        recruit_id: int = int(request.json['recruitId'])
        text: str = str(request.json['text'])
        step_num: int = int(request.json['stepNum'])
    except (KeyError, ValueError):
        return {'msg': 'Invalid data'}, 400

    comment: Comment = Comment(
        recruit_id=recruit_id,
        text=text,
        step_num=step_num,
    )
    session.add(comment)
    session.commit()

    return {
        'id': comment.id,
        'recruitId': comment.recruit_id,
        'text': comment.text,
        'stepNum': comment.step_num,
    }, 201


@common.route('/common/get_comments_by_recruit_step', methods=['GET'])
@jwt_required()
@swag_from({
    'tags': ['Common'],
    'summary': 'Get Comments by Recruit Step',
    'description': 'Endpoint to get comments by a recruit\'s step.',
    'parameters': [
        {
            'name': 'recruitId',
            'in': 'query',
            'type': 'integer',
            'required': True,
            'description': 'ID of the recruit to fetch comments for.'
        },
        {
            'name': 'stepNum',
            'in': 'query',
            'type': 'integer',
            'required': True,
            'description': 'Step number to fetch comments for.'
        }
    ],
    'responses': {
        200: {'description': 'List of comments for the recruit\'s step'},
    }
})
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
@swag_from({
    'tags': ['Common'],
    'summary': 'Get Recruit File',
    'description': 'Endpoint to get recruit file.',
    'parameters': [
        {
            'name': 'recruitId',
            'in': 'query',
            'type': 'integer',
            'required': True,
            'description': 'ID of the recruit to fetch file for.'
        }
    ],
    'responses': {
        200: {'description': 'Recruit file retrieved successfully'},
        400: {'description': 'Invalid data provided'},
    }
})
def get_recruit_file():
    try:
        recruit_id: int = int(request.args['recruitId'])
    except (KeyError, ValueError):
        return {'msg': 'Invalid data'}, 400

    path = './recruits/' + str(recruit_id)
    return send_from_directory('media', path)
