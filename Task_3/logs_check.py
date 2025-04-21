from pathlib import Path
import os
from collections import Counter
from typing import List, Dict, Optional

"""the func takes lines separated by \n
and values separated by space,
parse it into key named dict values and returned the dicts as a list"""


def parse_log_line(log: str) -> List[Dict[str, str]]:
    lines = log.strip().split('\n')
    records = []
    for line in lines:
        values = line.strip().split(' ')
        record = {
            "date": values[0] if len(values) > 0 else "",
            "time": values[1] if len(values) > 1 else "",
            "error type": values[2] if len(values) > 2 else "",
            "message": " ".join(values[3:]) if len(values) > 3 else ""
        }
        records.append(record)
    return records


"""the func takes full path to a log text,
checks if it's ok to be opened and return lines"""


def load_logs(path: Path) -> List:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File '{file_path}' does not exist.")
    if not file_path.is_file():
        raise ValueError(f"'{file_path}' is not a file.")
    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"File '{file_path}' is not readable.")
    if file_path.stat().st_size == 0:
        raise ValueError(f"File '{file_path}' is empty.")

    try:
        with file_path.open("r", encoding="utf-8") as file:
            content = file.read()
        return content
    except UnicodeDecodeError:
        raise UnicodeDecodeError("Invalid UTF-8 in log file.")


"""the func filters the parsed by 'parse_log_line' an output list
with a gotten required log level"""


def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    return [log for log in logs if log['error type'].lower() == level.lower()]


"""counts 'error type' values in the parsed by 'parse_log_line'
 an output list and return error type's keys and counted values"""


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    return dict(Counter(log['error type'] for log in logs))


def display_log_counts(counts: Dict[str, int], logs: Optional[List[Dict[str, str]]] = None, level: Optional[str] = None):
    if not counts:
        print("No log counts to display.")
        return

    purple = "\033[95m"
    reset = "\033[0m"

    print("\nРівень логування | Кількість")
    print("-----------------|----------")

    sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

    for error_type, count in sorted_counts:
        if level and error_type.lower() == level.lower():
            print(f"{purple}{error_type:<17}{reset}| {count}")
        else:
            print(f"{error_type:<17}| {count}")

    if level and logs:
        detailed_logs = filter_logs_by_level(logs, level)
        if detailed_logs:
            print(f"\nДеталі логів для рівня {purple}{level.upper()}{reset}:")
            for log in detailed_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
