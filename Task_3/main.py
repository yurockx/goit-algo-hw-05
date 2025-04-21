import sys
import logs_check
from typing import Optional


def run(file_path: str, e_level: Optional[str] = None):
    try:
        logs = logs_check.load_logs(file_path)
        parsed_logs = logs_check.parse_log_line(logs)
        counts = logs_check.count_logs_by_level(parsed_logs)
        logs_check.display_log_counts(counts, parsed_logs, e_level)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        run(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        print("Only two commands can be used! path/to/file and errorlevel")
        print("python main.py <directory/path>")
        print("Or python main.py <directory/path> errorlevel")
