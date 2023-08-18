from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from pro_filer.cli_helpers import _get_printable_file_path


def test_show_disk_usage(tmp_path, capsys):
    file1 = tmp_path / "file1.txt"
    file1.touch()
    file1.write_text("Teste arquivo 1")

    file2 = tmp_path / "file2.txt"
    file2.touch()
    file2.write_text("Teste 2")

    context = {"all_files": [str(file1), str(file2)]}

    output_one = f"'{_get_printable_file_path(str(file1))}':".ljust(
        70
    )
    output_two = f"'{_get_printable_file_path(str(file2))}':".ljust(
        70
    )

    show_disk_usage(context)
    captured = capsys.readouterr()
    assert (
        captured.out
        == f"{output_one} 15 (68%)\n{output_two} 7 (31%)\nTotal size: 22\n"
    )


def test_show_disk_usage_empty(capsys):
    empty_context = {"all_files": []}

    show_disk_usage(empty_context)
    captured = capsys.readouterr()
    assert captured.out == "Total size: 0\n"
