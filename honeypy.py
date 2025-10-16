# librarires 
import logging
from logging.handlers import RotatingFileHandler
import os




# constants
logging_format = logging.Formatter('%(message)s')

# loggers annd kogin files 
funnel_logger = logging.getLogger('FunnelLogger')
funnel_logger.setLevel(logging.INFO)
funnel_handler = RotatingFileHandler('audits.log', maxBytes=2000, backupCount=5)
funnel_handler.setFormatter(logging_format)
funnel_logger.addHandler(funnel_handler)

creds_logger = logging.getLogger('FunnelLogger')
creds_logger.setLevel(logging.INFO)
creds_handler = RotatingFileHandler('audits.log', maxBytes=2000, backupCount=5)
creds_handler.setFormatter(logging_format)
creds_logger.addHandler(funnel_handler)
# emulate shell
# ssh server + sockets
# provision ssh-based honeypot
