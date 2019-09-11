import sys
import os


def find_python_venv_path():
    """
    This is used as the base location to find the rest of the executables from GDAL and mapnik

    :return:
    """
    return os.path.basename(sys.executable)

def get_config():
    """
    Get the global config object
    :return:
    """

    venv_path = find_python_venv_path()

    return {

    }