import os
import sys


def is_validate_format_txt(path_file):
    _, format = os.path.splitext(path_file)
    if format != '.txt':
        return False
    return True


def txt_importer(path_file):
    is_validated = is_validate_format_txt(path_file)
    if is_validated:
        try:
            with open(path_file) as f:
                return f.read().split("\n")
        except FileNotFoundError:
            print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    else:
        print('Formato inválido', file=sys.stderr)
