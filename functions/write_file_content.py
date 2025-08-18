import os


def write_file_content(working_directory, file_path, content):
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(os.path.dirname(target_file)):
        try:
            os.makedirs(os.path.dirname(target_file))
        except Exception as e:
            return f"Error: {e}"

    try:
        with open(target_file, "w") as file:
            file.write(content)
    except Exception as e:
        return f"Error: {e}"

    return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"
