import os

class Config(object):
	SECRET_KEY=os.environ.get('Something') or b'\xb1\x1b|\x7f\x91\xc9\x93\t\x86\x03L\x83\x9c\xfc\xf2\x0c'
	MONGODB_SETTINGS={'db':'NewsCast'}