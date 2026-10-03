"""Conservative offline guard for accidental additions to this public scaffold."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", ".pytest_cache"}
ROOT_FILES = {
    "README.md", "README.en.md", "LICENSE", "NOTICE.md", "CONTRIBUTING.md",
    "SECURITY.md", "CHANGELOG.md", "pyproject.toml", ".gitignore", ".gitattributes", "llms.txt",
}
ROOT_DIRS = {".github", "assets", "docs", "scripts", "tests", "xuewuzhi_downloader"}
EXTENSIONS = {".md", ".py", ".json", ".toml", ".yml", ".yaml", ".svg", ".png", ".txt"}
SECRET_PATTERNS = (
    re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{30,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?i)(?:access_token|refresh_token|password|secret)\s*[=:]\s*[\"'][A-Za-z0-9+/=_-]{16,}"),
    re.compile(r"(?im)^\s*(?:from|import)\s+(?:Mooc|Login|xuewuzhi_runtime)(?:\.|\s|$)"),
)


def inspect_file(relative, data):
    issues = []
    if relative.parts[0] not in ROOT_DIRS and relative.as_posix() not in ROOT_FILES:
        issues.append("unexpected top-level path")
    if relative.as_posix() not in ROOT_FILES and relative.suffix.lower() not in EXTENSIONS:
        issues.append("file type is not approved for source publication")
    if any(part.startswith(".env") for part in relative.parts):
        issues.append("environment file")
    if len(data) > 2 * 1024 * 1024:
        issues.append("file exceeds 2 MiB public-source limit")
    if relative.suffix.lower() == ".png":
        if not data.startswith(b"\x89PNG\r\n\x1a\n"):
            issues.append("invalid image signature")
    else:
        try:
            content = data.decode("utf-8")
        except UnicodeDecodeError:
            issues.append("unexpected binary or non-UTF-8 text")
        else:
            if any(pattern.search(content) for pattern in SECRET_PATTERNS):
                issues.append("possible credential or private module dependency")
    return issues


def main():
    findings, checked = [], 0
    for path in sorted(ROOT.rglob("*")):
        relative = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in relative.parts):
            continue
        if path.is_symlink():
            findings.append((relative, ["symlink is not allowed"]))
        elif path.is_file():
            checked += 1
            issues = inspect_file(relative, path.read_bytes())
            if issues:
                findings.append((relative, issues))
    for path, issues in findings:
        print("FAIL {}: {}".format(path.as_posix(), "; ".join(issues)))
    if findings:
        return 1
    print("PASS: {} public files checked; no guarded patterns found.".format(checked))
    return 0


if __name__ == "__main__":
    sys.exit(main())
