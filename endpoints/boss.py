from flask import Blueprint

__all__ = (
    'boss',
)

boss: Blueprint = Blueprint('boss', __name__)


@boss.route('/boss/register_hr', methods=['POST'])
def register_hr():
    pass


@boss.route('/boss/get_hrs', methods=['GET'])
def get_hrs():
    pass


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
