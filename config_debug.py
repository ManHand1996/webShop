import os
from secrets import token_bytes
import datetime

FLASK_APP = 'app'
SECRET_KEY = b"\xd7\xd8fn\xf9'\xa0\x1c\xcev\x1d-av\xe70\x89A1vt9n\xa5\x91\x99\xb5\xba\x1e\xfeP\xb8"
JWT_AUTH_URL_RULE = '/api/auth'
JWT_TOKEN_LOCATION = ('cookies','headers')
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)
JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=30)
TIME_ZONE = 'Asia/Shanghai'
SQLALCHEMY_DATABASE_URI = 'mysql://manhand:manhand@127.0.0.1:3306/webshop'