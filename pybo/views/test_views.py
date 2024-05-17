from flask import Flask, Blueprint, render_template, request

bp = Blueprint("test", __name__, url_prefix="/test")
import time
import os
from datetime import datetime
import random
import string



@bp.route("/deletefile")
def deletefile():
    os.remove("pybo/static/upload/hello.js")
    return "hello"


@bp.route("/upload_ajax", methods=("POST",))
def upload_ajax():
    file = request.files["zzz"]
    filename = file.filename

    filename = make_new_name(filename)
    upload_path = makedirectory()

    path = os.path.join(upload_path, filename)

    file.save(path)

    idx = path.find("/static/upload")

    return path[idx:]


@bp.route("/upload", methods=("POST",))
def upload():
    file = request.files["file"]
    filename = file.filename

    filename = make_new_name(filename)

    upload_path = makedirectory()

    path = os.path.join(upload_path, filename)
    path = path.replace("\\","/")
    file.save(path)
    idx = path.find("/static/upload")
    return path[idx:]


@bp.route("/uploadform")
def uploadform():
    return render_template("test/file_upload.html")


def extract_origin_name():
    new_name = make_new_name("hello.jpg")
    print(new_name)

    return new_name[26:]


def make_new_name(name):
    letters = string.ascii_lowercase

    rnd_name = [random.choice(letters) for i in range(10)]
    print(rnd_name)

    msg = "".join(rnd_name)
    name_ymdhms = datetime.now().strftime("%Y%m%d%H%M%S")
    
    return msg+"_"+name_ymdhms+"_"+name


def makedirectory():
    UPLOAD_DIR="pybo/static/upload"
    name_ymd = datetime.now().strftime("%Y%m%d")
    
    new_dir_path = os.path.join(UPLOAD_DIR, name_ymd)

    if not os.path.exists(new_dir_path):
        os.mkdir(new_dir_path)

    return new_dir_path


@bp.route("/checkid/<id>")
def chechid(id):
    return id+": test"


@bp.route("/check_id_form")
def check_id_form():
    return render_template("test/check_id.html")


def monitor(func):
    def wrapper(*atgs, **kwargs):
        start = time.time()
        func()
        end = time.time()

        return str(end-start)
    return wrapper


@monitor
def hello():
    for i in range(100):
        print("world")

    return "hello"


@bp.route("/deco")
def deco():
    return hello()