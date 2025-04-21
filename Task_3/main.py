import sys
import logs_check
from pathlib import Path
from typing import Optional


def run(file_path, e_level=None):
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
        print("Use correct commands: python main.py <directory/path> ->with no spaces otherwise add quotes")
        print("Or add an error level to see mor details like: <directory/path>space>errorlevel")
