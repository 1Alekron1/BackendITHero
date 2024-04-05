import os

from flask import Blueprint, request
from config import UPLOAD_RECRUITS_FOLDER
from models import session, Recruit

__all__ = ("hr",)

hr: Blueprint = Blueprint("hr", __name__)


@hr.route("/hr/upload_recruits", methods=["POST"])
def upload_recruits():
    if "file" not in request.files:
        return {"msg": "No file"}, 400
    task_id = request.json().get("taskId", None)
    for filename in request.files:
        file = request.files[filename]
        if file.filename.endswith(".pdf"):
            file.save(os.path.join(UPLOAD_RECRUITS_FOLDER, file.filename))
            recruit: Recruit = Recruit(
                task_id=task_id, file_path=UPLOAD_RECRUITS_FOLDER + file.filename
            )
            session.add(recruit)
    session.commit()
    recruits = []
    for recruit in session.query(Recruit).filter_by(task_id=task_id):
        recruits.append(
            {
                "id": recruit.id,
                "taskId": recruit.task_id,
                "stepNum": recruit.step_num,
                "fileUrl": "...",
                "gotOffer": recruit.got_offer,
            }
        )

    return recruits, 200


@hr.route("/hr/update_recruit_step", methods=["PUT"])
def update_recruit_step():
    step_num = request.json.get("stepNum", None)
    recruit_id = request.json.get("recruitId", None)
    recruit = session.query(Recruit).filter_by(id=recruit_id).first()
    if not recruit:
        return {"msg": "No such recruit"}, 400
    recruit.step_num = step_num
    session.add(recruit)
    session.commit()
