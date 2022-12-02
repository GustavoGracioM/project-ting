from ting_file_management.queue import Queue


def occurrences_exists(lines, word):
    result = []
    for s in range(len(lines)):
        if word in lines[s].lower():
            result.append({"linha": s + 1})
    return result


def occurrences_search(lines, word):
    result = []
    for s in range(len(lines)):
        if word in lines[s].lower():
            result.append({"linha": s + 1, "conteudo": lines[s]})
    return result


def occurrences(word: str, instance: Queue, type_occurrences):
    list_occurrences = []
    for i in range(len(instance)):
        lines = instance.search(i)["linhas_do_arquivo"]
        content_lines = type_occurrences(lines, word)
        if len(content_lines) > 0:
            list_occurrences.append(
                {
                    "palavra": word,
                    "arquivo": instance.search(i)["nome_do_arquivo"],
                    "ocorrencias": content_lines,
                }
            )
    return list_occurrences


def exists_word(word: str, instance: Queue):
    return occurrences(word, instance, occurrences_exists)


def search_by_word(word, instance):
    return occurrences(word, instance, occurrences_search)
