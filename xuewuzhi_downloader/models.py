"""Small, independent data types for documenting component boundaries."""

from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class ResourceKind(str, Enum):
    VIDEO = "video"
    AUDIO = "audio"
    DOCUMENT = "document"


@dataclass(frozen=True)
class Resource:
    title: str
    kind: ResourceKind
    filename: str


@dataclass(frozen=True)
class Chapter:
    title: str
    resources: Tuple[Resource, ...]


@dataclass(frozen=True)
class Course:
    title: str
    chapters: Tuple[Chapter, ...]


@dataclass(frozen=True)
class Progress:
    completed: int
    total: int
    message: str
