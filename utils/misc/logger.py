import os
import logging
from sys import platform
import coloredlogs


def create_log_file():
    if not os.path.exists('utils/logs/iwth.log'):
        os.makedirs('utils/logs', 0o754, exist_ok=True)
        if platform == "linux" or platform == "linux2":
            os.mknod('utils/logs/iwth.log')
        elif platform == "win32":
            with open('utils/logs/iwth.log', 'w'): pass


# Init log directory and file if not exists
create_log_file()

# Set up logging to file
logging.basicConfig(level=logging.DEBUG,
                    format=u'[%(asctime)s] #%(levelname)-8s %(name)-14s | %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='utils/logs/iwth.log',
                    filemode='w'
                    )

# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)

# set a format for console use
formatter = logging.Formatter(u'%(filename)-14s: [LINE:%(lineno)d] #%(levelname)-8s %(message)s')
console.setFormatter(formatter)

# Color logs output
coloredlogs.install()

# add the handler to the root logger
logging.getLogger('').addHandler(console)

# Color logs output
coloredlogs.install()

# Now, we can log to the root logger, or any other logger. First the root...
logging.warning('Created by Steio Dev')
logging.info("Logger started successfully")



