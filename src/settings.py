sites = (
    'http://www.logiterm.pl/',
    'http://www.sas.busko.pl/pl/',
    'http://enix.pl/',
    'http://www.biawar.com.pl/',
    'http://www.elektromet.com.pl/',
    'http://www.vaillant.pl/',
    'http://www.junkers.pl/pl/pl/start/',
    'http://www.dedietrich.pl/'
)

download_types = (
    'short_info',
    'long_info',
    'image'
)

url = 'http://demo.opencart.com/admin/'

admin = {
    'user': 'demo',
    'pass': 'demo'
}

try:
    from src.local_settings import *
except ImportError:
    pass