from multiprocessing import Queue
from mythschedmini.command import CommandProcess

import os
basedir = os.path.abspath(os.path.dirname(__file__))

from localconfig import LocalConfig

class Config(LocalConfig):
    COMMAND_QUEUE = Queue()
    CONVERTER_PROCESS = None

    @staticmethod
    def init_app(app):
        if not Config.CONVERTER_PROCESS:
            p = CommandProcess(Config.COMMAND_QUEUE)
            Config.CONVERTER_PROCESS = p
            p.start()

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development' : DevelopmentConfig,
    'production' : ProductionConfig,
    'default' : DevelopmentConfig
}
