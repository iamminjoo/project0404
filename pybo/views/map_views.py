from flask import Flask, Blueprint, render_template

bp = Blueprint("map", __name__, url_prefix="/map")


@bp.route("/maplist")
def map_list():

    card = [
    {
        'title' : '강동구 공원안내',
        'text' : '강동구 공원 안내지도',
        'img' :  'gangdog.jpg',
        'map' : 'gd_park',
        'url' : 'https://www.gangdong.go.kr'
    },
    {
        'title' : '관광안내소',
        'text' : '서울 관광안내소 안내지도',
        'img' : 'logo_sto.jpg',
        'map' : 'map',
        'url' : 'https://www.sto.or.kr/index'
    },
    {
        'title' : '서울 인구수',
        'text' : '서울 인구분포 안내지도',
        'img' : 'seoul.png',
        'map' : 'people',
        'url' : 'https://www.seoul.go.kr/main/index.jsp'
    }
    ]

    return render_template("/test_map/map_list.html", card = card)


@bp.route("/mapcard/<info_map>")
def map_card(info_map):

    return render_template(f'/test_map/{info_map}.html')