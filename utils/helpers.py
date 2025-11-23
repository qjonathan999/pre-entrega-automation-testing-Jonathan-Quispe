import os

def get_file_path(file_name, folder="data"):
    import os
    current_file = os.path.dirname(__file__)
    file_path = os.path.join(current_file, "..", folder, file_name)
    return os.path.abspath(file_path)