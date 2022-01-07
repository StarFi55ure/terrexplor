import os


class BaseProcessor:

    def __init__(self):
        self._final_file = None

    @property
    def final_file(self):
        return os.path.abspath(self._final_file)

    def show_progress(self, line):
        print(line)
