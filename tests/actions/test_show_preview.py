from pro_filer.actions.main_actions import show_preview  # NOQA
import pytest


@pytest.mark.parametrize(
    "context, result_one, result_two, result_three",
    [
        (
            {
                "all_files": ["1", "2"],
                "all_dirs": [],
            },
            "Found 2 files and 0 directories",
            "First 5 files: ['1', '2']",
            "First 5 directories: []",
        ),
        (
            {
                "all_files": [],
                "all_dirs": ["1", "2"],
            },
            "Found 0 files and 2 directories",
            "First 5 files: []",
            "First 5 directories: ['1', '2']",
        ),
        (
            {
                "all_files": ["1", "2", "3", "4", "5", "6"],
                "all_dirs": ["1", "2", "3", "4", "5", "6"],
            },
            "Found 6 files and 6 directories",
            "First 5 files: ['1', '2', '3', '4', '5']",
            "First 5 directories: ['1', '2', '3', '4', '5']",
        ),
    ],
)
def test_show_preview(capsys, context, result_one, result_two, result_three):
    show_preview(context)
    captured = capsys.readouterr()
    assert result_one in captured.out
    assert result_two in captured.out
    assert result_three in captured.out
