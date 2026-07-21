"""Tests for week01/02/main.py and its companion CSV-style log file.

main.py is a top-level script (no functions/classes) that:
  1. Opens 'mission_computer_main.log' from the current working directory
     and reads its full contents into `logs` (only FileNotFoundError is
     caught here).
  2. Splits `logs` on the literal two-character string "/n" (NOT a real
     newline "\n") into `log_list` and prints it.
  3. Calls `log_list.sort()` -- which sorts in place and returns None -- and
     stores that None into `sorted_list`.
  4. Calls `sorted_list.reverse()`, which raises AttributeError because
     `sorted_list` is None.

These tests characterize the script's actual (buggy) behavior via
subprocess, since it has no importable functions and this PR's scope does
not include fixing the underlying bugs.
"""

import csv
import subprocess
import sys
from datetime import datetime
from pathlib import Path

WEEK01_02_DIR = Path(__file__).resolve().parent
MAIN_SCRIPT = WEEK01_02_DIR / "main.py"
LOG_FILE = WEEK01_02_DIR / "mission_computer_main.log"


def run_main(cwd):
    """Run main.py with the given working directory and capture the result."""
    return subprocess.run(
        [sys.executable, str(MAIN_SCRIPT)],
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=10,
    )


class TestMainScriptWithLogPresent:
    """main.py is run from its own directory, where the log file exists."""

    def test_exits_with_error_due_to_sort_reverse_bug(self):
        result = run_main(WEEK01_02_DIR)
        assert result.returncode != 0

    def test_traceback_reports_attribute_error_on_none(self):
        result = run_main(WEEK01_02_DIR)
        assert "AttributeError" in result.stderr
        assert "'NoneType' object has no attribute 'reverse'" in result.stderr

    def test_prints_log_list_before_crashing(self):
        result = run_main(WEEK01_02_DIR)
        log_content = LOG_FILE.read_text(encoding="utf-8")
        # The split uses the literal substring "/n" rather than a real
        # newline, so the whole file content ends up as a single list
        # element that gets printed verbatim (as part of a repr'd list).
        assert log_content.splitlines()[0] in result.stdout

    def test_produces_no_stdout_after_the_crash_point(self):
        # sorted_list/reversed_list are never printed because the script
        # crashes on the reverse() call before reaching any further output.
        result = run_main(WEEK01_02_DIR)
        assert "sorted_list" not in result.stdout
        assert "reversed_list" not in result.stdout


class TestMainScriptWithoutLogFile:
    """main.py is run from a directory that has no log file."""

    def test_prints_file_not_found_message(self, tmp_path):
        result = run_main(tmp_path)
        assert "Error: The log file does not exist." in result.stdout

    def test_exits_with_error_due_to_undefined_logs_variable(self, tmp_path):
        result = run_main(tmp_path)
        assert result.returncode != 0
        assert "NameError" in result.stderr
        assert "logs" in result.stderr


class TestSplitOnLiteralSlashN:
    """Documents/regresses the "/n" vs "\\n" split bug using the real file."""

    def test_log_file_contains_no_literal_slash_n(self):
        log_content = LOG_FILE.read_text(encoding="utf-8")
        assert "/n" not in log_content

    def test_split_on_literal_slash_n_yields_single_element(self):
        log_content = LOG_FILE.read_text(encoding="utf-8")
        log_list = log_content.split("/n")
        assert len(log_list) == 1
        assert log_list[0] == log_content

    def test_split_on_real_newline_would_yield_many_lines(self):
        # Sanity check contrasting the bug with the presumably intended
        # behavior: splitting on an actual newline produces one entry per
        # log line (header + 35 data rows).
        log_content = LOG_FILE.read_text(encoding="utf-8")
        lines = log_content.split("\n")
        assert len(lines) > 1


class TestMissionComputerLogFile:
    """Sanity-check the structure of the CSV-style log data used by main.py."""

    def test_file_exists(self):
        assert LOG_FILE.is_file()

    def test_header_row(self):
        with LOG_FILE.open(encoding="utf-8") as f:
            header = f.readline().strip()
        assert header == "timestamp,event,message"

    def test_every_row_has_three_columns(self):
        with LOG_FILE.open(encoding="utf-8", newline="") as f:
            rows = list(csv.reader(f))
        assert len(rows) > 1
        for row in rows[1:]:
            assert len(row) == 3

    def test_timestamps_are_parseable_and_chronologically_sorted(self):
        with LOG_FILE.open(encoding="utf-8", newline="") as f:
            rows = list(csv.DictReader(f))
        timestamps = [
            datetime.strptime(row["timestamp"], "%Y-%m-%d %H:%M:%S")
            for row in rows
        ]
        assert len(timestamps) > 1
        assert timestamps == sorted(timestamps)

    def test_contains_expected_anomaly_and_milestone_entries(self):
        text = LOG_FILE.read_text(encoding="utf-8")
        assert "Liftoff! Rocket has left the launchpad." in text
        assert "Oxygen tank unstable." in text
        assert "Oxygen tank explosion." in text
        assert "Center and mission control systems powered down." in text