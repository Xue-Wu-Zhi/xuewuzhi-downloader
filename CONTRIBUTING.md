# 参与贡献

欢迎改进使用文档、无账号的离线示例、公开目录、无障碍体验与问题模板。

1. 先查看相关 Wiki 和已有 Issue，说明改动要解决的问题。
2. 从 `main` 建立分支。公开平台元数据位于 `xuewuzhi_downloader/data/platforms.json`。
3. 本地运行 `python -m xuewuzhi_downloader demo`、`python -m unittest discover -s tests -v` 和 `python scripts/check_public_tree.py`。
4. 提交简洁的 PR，说明用户可见变化和验证结果。文档链接尽量使用相对地址。

不要提交真实账号、Cookie、令牌、验证码、课程媒体、内部接口地址或官方客户端源码。示例数据必须虚构。需要新增平台支持时，提交不含隐私的平台名称、公开官网和用户需求；本仓库不接收专有客户端适配器实现。

Wiki 的可审阅副本放在 `docs/wiki/`。修改副本后，由维护者在发布时批量同步到 GitHub Wiki。不要把开发环境或下载目录一起提交。
