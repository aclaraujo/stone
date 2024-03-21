#!/usr/bin/env python3

import os.path
import sys
from logging import Logger

import requests
import logging
from util import extract_csv

logger: Logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)

_url_file = "https://dadosabertos.rfb.gov.br/CNPJ/{file_name}.zip"
_file_path = "files/{file_name}.zip"


def get_file(file_name):
    file_path = _file_path.format(file_name=file_name)
    url_file = _url_file.format(file_name=file_name)
    if not os.path.isfile(file_path):
        logger.info(f'Downloading file {file_path}')
        requests.get(url_file)
        logger.info(f'Download file {file_path} done')

    logger.info(f'Starting extract file {file_path}')
    extract_csv(file_path, "files/csv")


def main():
    get_file("Empresas9")
    get_file("Socios9")


if __name__ == '__main__':
    main()