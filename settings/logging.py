from settings.base import *

LOG_FILE_NAME = 'app.log'

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s  - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, LOG_FILE_NAME),
            'formatter': 'standard'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        }
    },
    'loggers': {
        'app': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
        },
    },
}