"""A fixed, fictional course; no account, network or media access."""

from .models import Chapter, Course, Resource, ResourceKind


class DemoProvider:
    def list_courses(self):
        return (
            Course(
                title="示例课程 · 学习方法入门",
                chapters=(
                    Chapter("01 建立学习计划", (
                        Resource("学习目标", ResourceKind.VIDEO, "01 学习目标.mp4"),
                        Resource("练习讲义", ResourceKind.DOCUMENT, "02 练习讲义.pdf"),
                    )),
                    Chapter("02 回顾与复习", (
                        Resource("章节回顾", ResourceKind.VIDEO, "01 章节回顾.mp4"),
                        Resource("复习音频", ResourceKind.AUDIO, "02 复习音频.mp3"),
                    )),
                ),
            ),
        )


def describe(course):
    lines = [course.title + "/"]
    for index, chapter in enumerate(course.chapters):
        last = index == len(course.chapters) - 1
        lines.append(("└── " if last else "├── ") + chapter.title + "/")
        prefix = "    " if last else "│   "
        for number, resource in enumerate(chapter.resources):
            branch = "└── " if number == len(chapter.resources) - 1 else "├── "
            lines.append(prefix + branch + resource.filename)
    return "\n".join(lines)
