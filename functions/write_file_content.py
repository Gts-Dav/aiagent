import os
from google.genai import types


write_file_content_schema = types.FunctionDeclaration(
    name="write_file_content",
    description="Writes the content to the given file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write the content to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the given file."
            ),
        },
    ),
)


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
