"""Arquivo que estudantes devem editar"""

"""Utilização da função lambda para criar uma função anônima que recebe vários
argumentos: https://pythonacademy.com.br/blog/funcoes-lambda-no-python"""


def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        deepest_file = max(
            context["all_files"],
            key=lambda path: len(path.split("/")),
        )
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        if (
            not case_sensitive and search_term.lower() in file_name.lower()
        ) or (case_sensitive and search_term in file_name):
            found_files.append(path)

    return found_files
