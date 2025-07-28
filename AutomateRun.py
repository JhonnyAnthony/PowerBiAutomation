import logging
from src.Load.dict import (
    dict_extract
)

from src.Extract.main import Automate
from src.Load.logs import Logs
if __name__ == "__main__":
    # Configuração dos logs
    Logs.logs()
    Automate(**dict_extract["Azure"]).run()