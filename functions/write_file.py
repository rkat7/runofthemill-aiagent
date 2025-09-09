import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: "{file_path}" is not in the working directory'

    parent_dir = os.path.dirname(abs_file_path)
    if not os.path.isdir(parent_dir):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return "Couldn't create parent dirs: {parent_dir} = {e}"

    try:
        with open(abs_file_path, 'w') as f:
            f.write(content)
        return f'File "{abs_file_path}" has been written to "{abs_working_dir}"'
    except Exception as e:
        return f"Couldn't write file: {e}"
