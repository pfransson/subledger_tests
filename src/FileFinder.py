import os
import fnmatch

class FileFinder:
    @staticmethod
    def get_files(folder_path, file_type):
        matches = []
        for root, dirnames, filenames in os.walk(folder_path):
            for filename in fnmatch.filter(filenames, '*.' + file_type):
                matches.append(os.path.join(root, filename))
        return matches
    
    @staticmethod
    def get_filename(filepath):
        return os.path.basename(filepath)
