# ---------------------------------------- [edit] ---------------------------------------- #
from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'8\xfd\x96\x01\xc7D\x9e\xbc}\\\xd0\xadH\xf7yF'
# ---------------------------------------------------------------------------------------- #