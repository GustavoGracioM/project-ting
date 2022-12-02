import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def is_exits_file(path_file: str, instance: Queue):
    for i in range(len(instance)):
        if path_file == instance.search(i)['nome_do_arquivo']:
            return True
    return False


def process(path_file: str, instance: Queue):
    exits = is_exits_file(path_file, instance)
    if not exits:
        lines_txt = txt_importer(path_file)
        process_dict = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines_txt),
            "linhas_do_arquivo": lines_txt
        }
        instance.enqueue(process_dict)
        print(process_dict, file=sys.stdout)


def remove(instance: Queue):
    if instance.is_empty():
        return print('Não há elementos', file=sys.stdout)
    else:
        deleted = instance.dequeue()['nome_do_arquivo']
        print(f'Arquivo {deleted} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
