import os
from config import MAX_FILE_LENGTH


def get_file_content(working_directory, file_path):
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" is not a file'

    file_content = None
    try:
        with open(target_file, "r") as file:
            file_content = file.read(MAX_FILE_LENGTH)
    except Exception as e:
        return f"Error: {e}"

    if len(file_content) == MAX_FILE_LENGTH:
        file_content += f"[...File \"{file_path}\" truncated at {
            MAX_FILE_LENGTH} characters]"

    return file_content
