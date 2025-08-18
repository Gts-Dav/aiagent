import os


def get_files_info(working_directory, directory="."):
    target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    file_infos = []
    try:
        directory_contents = os.listdir(target_dir)
        for file_name in directory_contents:
            file_path = os.path.join(target_dir, file_name)
            file_infos.append(f"- {file_name}: file_size={os.path.getsize(
                file_path)} bytes, is_dir={os.path.isdir(file_path)}")
        return "\n".join(file_infos)
    except Exception as e:
        return f"Error: {e}"
