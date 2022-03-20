import os
from abc import ABC


class EnvLoader(ABC):
    def __init__(self):
        for env_name, env_type in self.__annotations__.items():
            self.__dict__[env_name] = env_type(os.getenv(env_name, ''))


class Settings(EnvLoader):
    TG_TOKEN: str
    YA_API_TOKEN: str


conf = Settings()
