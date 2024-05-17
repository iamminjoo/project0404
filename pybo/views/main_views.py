from flask import Flask, Blueprint , render_template, request, session, g
from pybo.models import Question, User

bp = Blueprint("main", __name__, url_prefix="/")

# 어떤요청이 들어오더라도 반드시 먼저 실행하는 코드 
@bp.before_app_request 
def set_g():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)
# 여기까지 선실행 코드

@bp.route("/")
def index():
    page = request.args.get("page", type=int, default=1)
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page=page, per_page=10)
    return render_template("question/question_list.html", question_list = question_list)