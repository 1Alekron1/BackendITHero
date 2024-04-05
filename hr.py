from flask import Blueprint

__all__ = (
    'hr',
)

hr: Blueprint = Blueprint('hr', __name__)


@hr.route('/hr/load_recruits_by_vacancy', methods=['POST'])
def load_recruits_by_vacancy():
    pass


@hr.route('/hr/get_recruits_by_vacancy', methods=['GET'])
def get_recruits_by_vacancy():
    pass


@hr.route('/hr/get_steps_by_recruit', methods=['GET'])
def get_steps_by_recruit():
    pass


@hr.route('/hr/update_steps_by_recruit', methods=['PUT'])
def update_steps_by_recruit():
    pass
