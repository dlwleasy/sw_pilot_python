"""Tests for week01/01/main.py and the accompanying documentation/log files.

main.py is a simple top-level script (no functions/classes) that:
  1. Prints "Hello Mars".
  2. Opens 'mission_computer_main.log' from the current working directory,
     reads it, and prints its contents.
  3. Catches FileNotFoundError (and, redundantly, two generic Exception
     handlers plus an unreachable PermissionError handler) if the file
     cannot be read.

Because the script has no importable functions, it is exercised end-to-end
via subprocess so that stdout/stderr/exit-code behavior can be verified
without mutating the real working directory of the test process.
"""

import re
import subprocess
import sys
from pathlib import Path

WEEK01_01_DIR = Path(__file__).resolve().parent
MAIN_SCRIPT = WEEK01_01_DIR / "main.py"
LOG_FILE = WEEK01_01_DIR / "mission_computer_main.log"
QUESTION_FILE = WEEK01_01_DIR / "question.md"
LOG_ANALYSIS_FILE = WEEK01_01_DIR / "log_analysis.md"


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

    def test_exits_successfully(self):
        result = run_main(WEEK01_01_DIR)
        assert result.returncode == 0

    def test_prints_hello_mars_first(self):
        result = run_main(WEEK01_01_DIR)
        assert result.stdout.startswith("Hello Mars\n")

    def test_prints_full_log_file_contents(self):
        result = run_main(WEEK01_01_DIR)
        log_content = LOG_FILE.read_text(encoding="utf-8")
        assert log_content in result.stdout

    def test_does_not_report_missing_file_error(self):
        result = run_main(WEEK01_01_DIR)
        assert "Error: The log file does not exist." not in result.stdout

    def test_produces_no_stderr_output(self):
        result = run_main(WEEK01_01_DIR)
        assert result.stderr == ""


class TestMainScriptWithoutLogFile:
    """main.py is run from a directory that has no log file."""

    def test_exits_successfully_even_without_log_file(self, tmp_path):
        result = run_main(tmp_path)
        assert result.returncode == 0

    def test_still_prints_hello_mars(self, tmp_path):
        result = run_main(tmp_path)
        assert "Hello Mars" in result.stdout

    def test_prints_file_not_found_message(self, tmp_path):
        result = run_main(tmp_path)
        assert "Error: The log file does not exist." in result.stdout

    def test_produces_no_stderr_output(self, tmp_path):
        result = run_main(tmp_path)
        assert result.stderr == ""


class TestQuestionMarkdown:
    """question.md describes the assignment; verify it moved intact."""

    def test_file_exists(self):
        assert QUESTION_FILE.is_file()

    def test_mentions_the_log_file_to_analyze(self):
        text = QUESTION_FILE.read_text(encoding="utf-8")
        assert "mission_computer_main.log" in text

    def test_mentions_exception_handling_requirement(self):
        text = QUESTION_FILE.read_text(encoding="utf-8")
        assert "예외" in text


class TestLogAnalysisMarkdown:
    """log_analysis.md is a placeholder analysis doc; verify it moved intact."""

    def test_file_exists(self):
        assert LOG_ANALYSIS_FILE.is_file()

    def test_file_is_not_empty(self):
        text = LOG_ANALYSIS_FILE.read_text(encoding="utf-8")
        assert text.strip() != ""


class TestMissionComputerLogFile:
    """Sanity-check the structure of the sample log data used by main.py."""

    LINE_PATTERN = re.compile(
        r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[[A-Z]+\] .+$"
    )

    def test_file_exists(self):
        assert LOG_FILE.is_file()

    def test_file_is_not_empty(self):
        assert LOG_FILE.read_text(encoding="utf-8").strip() != ""

    def test_every_line_matches_expected_log_format(self):
        lines = LOG_FILE.read_text(encoding="utf-8").splitlines()
        assert len(lines) > 0
        for line in lines:
            assert self.LINE_PATTERN.match(line), (
                f"Line does not match 'YYYY-MM-DD HH:MM:SS [LEVEL] message' "
                f"format: {line!r}"
            )

    def test_contains_expected_severity_levels(self):
        text = LOG_FILE.read_text(encoding="utf-8")
        for level in ("[INFO]", "[WARN]", "[ERROR]", "[CRITICAL]"):
            assert level in text