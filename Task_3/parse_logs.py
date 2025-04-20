def parse_log_line(log: str) -> dict:
    lines = log.strip().split('\n')
    values_dic = []
    for line in lines:
        values = line.strip().split(' ')
        dic_record = {
            "date": values[0] if len(values) > 0 else "",
            "time": values[1] if len(values) > 1 else "",
            "error type": values[2] if len(values) > 2 else "",
            "message": " ".join(values[3:]) if len(values) > 3 else ""
        }
        values_dic.append(dic_record)
    return values_dic

            # for line_number, line in enumerate(file, 1):
            #     if len(parts) != 3:
            #         return f"Error: Invalid data format on line {line_number} in '{file_path}'. Expected 'id,name,age'."
            #     cat_id, name, age_str = parts

            #     if not cat_id.strip():
            #         return f"Error: 'id' cannot be empty on line {line_number} in '{file_path}'."
            #     if not name.strip():
            #         return f"Error: 'name' cannot be empty on line {line_number} in '{file_path}'."
            #     if not age_str.strip().isdigit():
            #         return f"Error: 'age' must be a number on line {line_number} in '{file_path}'."