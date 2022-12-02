from ting_file_management.queue import Queue


def ocorrencias_in_lines(lines, word):
    pp = []
    for s in range(len(lines)):
        if word in lines[s].lower():
            pp.append({"linha": s + 1})
    return pp


def exists_word(word: str, instance: Queue):
    list_ocorrencias = []
    for i in range(len(instance)):
        lines = instance.search(i)['linhas_do_arquivo']
        content_lines = ocorrencias_in_lines(lines, word)
        if len(content_lines) > 0:
            list_ocorrencias.append({
                "palavra": word,
                "arquivo": instance.search(i)['nome_do_arquivo'],
                "ocorrencias": content_lines
            })
    return list_ocorrencias


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
