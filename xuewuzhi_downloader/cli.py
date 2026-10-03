"""Read-only CLI for exploring the public scaffold."""

import argparse
import json
from importlib.resources import files

from . import __version__
from .demo import DemoProvider, describe


def main(argv=None):
    parser = argparse.ArgumentParser(description="学无止公开骨架：离线示例与公开平台目录。")
    parser.add_argument("--version", action="version", version="scaffold " + __version__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("demo", help="打印虚构课程目录，不创建或下载媒体文件")
    platforms = commands.add_parser("platforms", help="查询官方客户端的公开教程目录")
    platforms.add_argument("--query", default="", help="按名称或分类筛选")
    args = parser.parse_args(argv)
    if args.command == "demo":
        print("[离线演示] 以下是虚构课程结构；未连接平台，未下载文件。\n")
        for course in DemoProvider().list_courses():
            print(describe(course))
        return 0
    catalog = json.loads(files("xuewuzhi_downloader").joinpath("data/platforms.json").read_text(encoding="utf-8"))
    query = args.query.casefold()
    rows = [row for row in catalog["entries"] if query in (row["name"] + row["category"]).casefold()]
    print("官方客户端公开目录；这些平台的适配器未包含在本仓库。")
    for row in rows:
        print("{name} | {category}\n  {guide_url}".format(**row))
    print("共 {} 个结果。".format(len(rows)))
    return 0
