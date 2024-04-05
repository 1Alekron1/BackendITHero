from flask import Blueprint

__all__ = (
    'common',
)

common: Blueprint = Blueprint('common', __name__)


@common.route('/common/get_tasks', methods=['GET'])
def get_tasks():
    pass


@common.route('/common/get_recruits_by_task', methods=['GET'])
def get_recruits_by_task():
    pass


@common.route('/common/get_steps_by_recruit', methods=['GET'])
def get_steps_by_recruit():
    pass


@common.route('/common/add_comment_to_recruit_step', methods=['POST'])
def add_comment_to_recruit_step():
    pass
