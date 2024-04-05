from flask import Blueprint

__all__ = (
    'hr',
)

hr: Blueprint = Blueprint('hr', __name__)


@hr.route('/hr/upload_recruits', methods=['POST'])
def upload_recruits():

    pass


@hr.route('/hr/update_recruit_step', methods=['PUT'])
def update_recruit_step():
    pass
