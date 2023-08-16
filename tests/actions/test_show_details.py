from pro_filer.actions.main_actions import show_details  # NOQA
from unittest.mock import Mock, patch
import pytest
import time

"""mktime method: https://www.geeksforgeeks.org/python-time-mktime-method/"""
time_stamp = time.mktime(
    time.strptime("2023-08-16", "%Y-%m-%d")
)


def test_show_details_file_not_found(capsys):
    mock_os_path_exists = Mock(return_value=False)
    file_path = {"base_path": "/home/trybe/????"}

    with patch("os.path.exists", mock_os_path_exists):
        show_details(file_path)
        captured = capsys.readouterr()
        assert captured.out == "File '????' does not exist\n"


@pytest.mark.parametrize(
    "context, name, size, type, extension, date",
    [
        (
            {"base_path": "/home/trybe/Downloads/Trybe_logo.png"},
            "File name: Trybe_logo.png\n",
            "File size in bytes: 100\n",
            "File type: file\n",
            "File extension: .png\n",
            "Last modified date: 2023-08-16\n",
        )
    ],
)
def test_show_details_file(capsys, context, name, size, type, extension, date):
    mock_os_path_exists = Mock(return_value=True)
    mock_os_path_getsize = Mock(return_value=100)
    mock_os_path_isdir = Mock(return_value=False)
    mock_os_path_splitext = Mock(return_value=("Trybe_logo", ".png"))
    mock_os_path_getmtime = Mock(return_value=time_stamp)

    with (
        patch("os.path.exists", mock_os_path_exists),
        patch("os.path.getsize", mock_os_path_getsize),
        patch("os.path.isdir", mock_os_path_isdir),
        patch("os.path.splitext", mock_os_path_splitext),
        patch("os.path.getmtime", mock_os_path_getmtime),
    ):
        show_details(context)
        captured = capsys.readouterr()
        assert captured.out == name + size + type + extension + date


@pytest.mark.parametrize(
    "context, name, size, type, extension, date",
    [
        (
            {"base_path": "/home/trybe/Downloads"},
            "File name: Downloads\n",
            "File size in bytes: 100\n",
            "File type: directory\n",
            "File extension: [no extension]\n",
            "Last modified date: 2023-08-16\n",
        )
    ],
)
def test_show_details_directory(
    capsys, context, name, size, type, extension, date
):
    mock_os_path_exists = Mock(return_value=True)
    mock_os_path_getsize = Mock(return_value=100)
    mock_os_path_isdir = Mock(return_value=True)
    mock_os_path_splitext = Mock(return_value=("Downloads", ""))
    mock_os_path_getmtime = Mock(return_value=time_stamp)

    with (
        patch("os.path.exists", mock_os_path_exists),
        patch("os.path.getsize", mock_os_path_getsize),
        patch("os.path.isdir", mock_os_path_isdir),
        patch("os.path.splitext", mock_os_path_splitext),
        patch("os.path.getmtime", mock_os_path_getmtime),
    ):
        show_details(context)
        captured = capsys.readouterr()
        assert captured.out == name + size + type + extension + date
