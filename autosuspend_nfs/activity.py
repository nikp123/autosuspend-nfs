import configparser
import os.path
from autosuspend.checks import Activity, ConfigurationError
from os import path


class ClientConnected(Activity):
    @classmethod
    def create(cls, name: str, config: configparser.SectionProxy) -> "ClientConnected":
        return cls(name)
        
    def __init__(self, name: str) -> None:
        Activity.__init__(self, name)

    def check(self):
        if os.listdir('/proc/fs/nfsd/clients'):
            return "Clients connected"
        else:
            return None
