import os

from flask import Blueprint, request
from config import UPLOAD_RECRUITS_FOLDER

__all__ = ("hr",)

hr: Blueprint = Blueprint("hr", __name__)


@hr.route("/hr/upload_recruits", methods=["POST"])
def upload_recruits():
    if "file" not in request.files:
        return {"msg": "No file"}, 400

    file = request.files["file"]
    if file.filename.endswith(".pdf"):
        file.save(os.path.join(UPLOAD_RECRUITS_FOLDER, file.filename))


@hr.route("/hr/update_recruit_step", methods=["PUT"])
def update_recruit_step():
    pass
