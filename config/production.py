from config.default import *

SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(
    os.path.join(BASE_DIR, 'pybo.db')

)

SQLALCHEMY_TRACK_MODIFICATION=False


SECRET_KEY=b'\xae\xdeo\xfb\x10\x90\xf7~#\x82\x1d\xe3\xads\xbbc'