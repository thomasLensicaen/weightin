import json
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin


@dataclass
class DbConfig(DataClassJsonMixin):
    host: str
    port: int


@dataclass
class AppConfig(DataClassJsonMixin):
    host: str
    port: int


@dataclass
class LogConfig(DataClassJsonMixin):
    filepath: str
    level: int


@dataclass
class Config(DataClassJsonMixin):
    db_config: DbConfig
    app_config: AppConfig
    log_config: LogConfig

    @staticmethod
    def from_file(path):
        with open(path,'r') as f:
            config_content = f.read()
            return Config.from_json(config_content)
