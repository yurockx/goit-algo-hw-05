import pathlib
import os
from colorama import Fore, init

init(autoreset=True)  #reset colors after each print

def get_cats_info(path):
    # Reads information about cats:) from a txt file and returns a list of dictionaries.
    # Each line in the file is expected to be in the format: id,name,age.
    # Args:
    #     path (str): The path to the txt file.
    # Returns:
    #     list[dict]: A list of dictionaries, where each dictionary represents a cat
    #                  and has keys 'id', 'name', and 'age'.
    file_path = pathlib.Path(path)

    # Check file integrity and availability
    if not file_path.exists():
        return f"Error: File '{file_path}' does not exist or the path is wrong."
    if not file_path.is_file():
        return f"Error: '{file_path}' is not a file."
    if not os.access(file_path, os.R_OK):
        return f"Error: File '{file_path}' is not readable."
    if file_path.stat().st_size == 0:
        return f"Error: File '{file_path}' is empty."

    list_cats_dics = []
    try:
        with file_path.open("r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                parts = line.strip().split(',')
                if len(parts) != 3:
                    return f"Error: Invalid data format on line {line_number} in '{file_path}'. Expected 'id,name,age'."
                cat_id, name, age_str = parts

                if not cat_id.strip():
                    return f"Error: 'id' cannot be empty on line {line_number} in '{file_path}'."
                if not name.strip():
                    return f"Error: 'name' cannot be empty on line {line_number} in '{file_path}'."
                if not age_str.strip().isdigit():
                    return f"Error: 'age' must be a number on line {line_number} in '{file_path}'."

                list_cats_dics.append({"id": cat_id.strip(), "name": name.strip(), "age": int(age_str.strip())})

        return list_cats_dics

    except UnicodeDecodeError:
        return f"Error: The file '{file_path}' is not a valid UTF-8 encoded text file."
    except Exception as e:
        return f"An unexpected error occurred while reading '{file_path}': {e}"




def load_logs(file_path: str) -> list:
    path = pathlib.Path(file_path)

    # Check file integrity and availability
    if not path.exists():
        return f"Error: File '{path}' does not exist or the path is wrong."
    if not path.is_file():
        return f"Error: '{path}' is not a file."
    if not os.access(path, os.R_OK):
        return f"Error: File '{path}' is not readable."
    if path.stat().st_size == 0:
        return f"Error: File '{path}' is empty."

    logs_dic = []
    try:
        with file_path.open("r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                parts = line.strip().split(',')
                if len(parts) != 3:
                    return f"Error: Invalid data format on line {line_number} in '{file_path}'. Expected 'id,name,age'."
                cat_id, name, age_str = parts

                if not cat_id.strip():
                    return f"Error: 'id' cannot be empty on line {line_number} in '{file_path}'."
                if not name.strip():
                    return f"Error: 'name' cannot be empty on line {line_number} in '{file_path}'."
                if not age_str.strip().isdigit():
                    return f"Error: 'age' must be a number on line {line_number} in '{file_path}'."

                list_cats_dics.append({"id": cat_id.strip(), "name": name.strip(), "age": int(age_str.strip())})

        return list_cats_dics
    
        except UnicodeDecodeError:
        return f"Error: The file '{file_path}' is not a valid UTF-8 encoded text file."
    except Exception as e:
        return f"An unexpected error occurred while reading '{file_path}': {e}"