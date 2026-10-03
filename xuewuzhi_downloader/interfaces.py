"""Illustrative contracts, not the proprietary client's API or plugin SDK."""

from typing import Iterable, Protocol

from .models import Course, Progress


class CourseProvider(Protocol):
    def list_courses(self) -> Iterable[Course]:
        """Return courses supplied by an independently implemented provider."""
        ...


class DownloadEngine(Protocol):
    def run(self, course: Course) -> Iterable[Progress]:
        """Contract only. No engine implementation ships in this repository."""
        ...
