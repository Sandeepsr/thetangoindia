import os
import logging

logger = logging.getLogger()


PROJECT_DIR = os.path.dirname((os.path.realpath(__file__)))
# logger.info(PROJECT_DIR)
PROJECT_BASE_DIR = os.path.abspath(os.path.join(
    PROJECT_DIR, os.pardir, os.pardir, os.pardir))
# logger.info(PROJECT_BASE_DIR)
SITE_PKG_PATH = os.path.join(PROJECT_BASE_DIR,
                             't/py34/lib/python3.4/site-packages/')

PAGE_IDS = ['264587550321500', '527770257327317', '291047664345550',
            '1636178923304872', '100006844149398',
            '197346010313291', '305372292817505', '107857822580692',
            '1513486182213415', '7213847061', '1099207956812482']


PAGE_IDS_DICT = {'264587550321500': 'Hyderabad',
                 '527770257327317': 'Bangalore',
                 '1636178923304872': 'Mumbai',
                 '100006844149398': 'Chennai',
                 '197346010313291': 'Auroville-Pondichery',
                 '305372292817505': 'Pune',
                 '107857822580692': 'Mumbai Tango',
                 '1099207956812482': 'Bangalore - Elcabeco',
                 '7213847061': 'New Delhi Tango'}

TANGO_LOCATION = {'264587550321500': 'Hyderabad',
                  '527770257327317': 'Bangalore',
                  '1636178923304872': 'Mumbai',
                  '100006844149398': 'Chennai',
                  '197346010313291': 'Auroville-Pondichery',
                  '305372292817505': 'Pune',
                  '107857822580692': 'Mumbai Tango',
                  '1099207956812482': 'Bangalore - Elcabeco',
                  '7213847061': 'NewDelhi - 2 To Tango',
                  '291047664345550': 'NDTS-New Delhi Tango School',
                  '1513486182213415': 'Mumbai - BTangoConscious',
                  '244450719272677': 'Goa Tango Community'}
                 
tango_location = {'264587550321500': 'Hyderabad', '527770257327317': 'Bangalore', '1636178923304872': 'Mumbai', '100006844149398': 'Chennai', '197346010313291': 'Auroville-Pondichery',
                  '305372292817505': 'Pune', '107857822580692': 'Mumbai Tango', '1099207956812482': 'Bangalore - Elcabeco', '7213847061': 'NewDelhi - 2 To Tango', '291047664345550': 'NDTS-New Delhi Tango School', '1513486182213415': 'Mumbai - BTangoConscious', '244450719272677': 'Goa Tango Community'}
