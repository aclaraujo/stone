import os.path
import sys

import requests

from util import extract_csv

_url_file = "https://dadosabertos.rfb.gov.br/CNPJ/{file_name}.zip"
_file_path = "files/{file_name}.zip"


def get_file(file_name):

    file_path = _file_path.format(file_name=file_name)
    url_file = _url_file.format(file_name=file_name)

    if not os.path.isfile(file_path):
        r = requests.get(url_file)

    extract_csv(file_path, "files/csv")


get_file("Empresas9")
get_file("Socios9")
