sites = {
    'logiterm': 'http://www.logiterm.pl/',
    'sas': 'http://www.sas.busko.pl/pl/',
    'enix': 'http://enix.pl/',
    'biawar': 'http://www.biawar.com.pl/',
    'elektromet': 'http://www.elektromet.com.pl/',
    'vaillant': 'http://www.vaillant.pl/',
    'junkers': 'http://www.junkers.pl/pl/pl/start/',
    'dedietrich': 'http://www.dedietrich.pl'
}

tmp_directory = 'tmp/'
url = 'http://demo.opencart.com/admin/'

admin = {
    'user': 'demo',
    'pass': 'demo'
}

try:
    from src.local_settings import *
except ImportError:
    pass