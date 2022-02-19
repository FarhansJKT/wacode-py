from flask import *
from requests import get, post, put
import datetime

wa = Flask('Whatsapp - Codes')
wa.config['app_secret'] = ''
wa.config['time_local'] = datetime.datetime.today()

@wa.route('/')
def rootIndex():
	return """<p align="center">Belum tersedia</p>"""

if __name__ == "__main__":
	wa.run(port=8080)
