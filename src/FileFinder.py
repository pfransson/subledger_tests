import os
import fnmatch

class FileFinder:
    def __init__(self, folder_path, file_type):
        self.folder_path = folder_path
        self.file_type = file_type

    def get_files(self):
        matches = []
        for root, dirnames, filenames in os.walk(self.folder_path):
            for filename in fnmatch.filter(filenames, '*.' + self.file_type):
                matches.append(os.path.join(root, filename))
        return matches