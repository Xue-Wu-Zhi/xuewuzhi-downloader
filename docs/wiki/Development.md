# 本地开发与验证


## 环境与运行

使用 Python 3.9 或更新版本。直接从仓库根目录运行，不需要安装第三方运行时依赖：

```bash
python -m xuewuzhi_downloader --version
python -m xuewuzhi_downloader demo
python -m xuewuzhi_downloader platforms --query MOOC
```

`demo` 只打印虚构课程目录。`platforms` 读取本地公开目录并按名称或分类筛选，命令不会检测远端平台是否可用。

如需安装命令行入口，可在自己的虚拟环境中执行 `python -m pip install -e .`，随后运行 `xuewuzhi-demo demo`。此步骤可能需要获取构建工具，但示例本身没有网络依赖。

## 项目结构

| 路径 | 修改场景 |
| --- | --- |
| `xuewuzhi_downloader/models.py` | 改进通用示例数据结构 |
| `xuewuzhi_downloader/interfaces.py` | 澄清抽象组件边界 |
| `xuewuzhi_downloader/demo.py` | 改善虚构课程演示 |
| `xuewuzhi_downloader/data/platforms.json` | 修正公开目录信息 |
| `docs/wiki/` | 修改可审阅的 Wiki 副本 |
| `tests/` | 检查离线行为和公开文件保护 |

## 验证命令

```bash
python -m unittest discover -s tests -v
python scripts/check_public_tree.py
```

测试检查示例在网络连接被禁止时仍能运行，目录查询能正确处理无结果情况，并检查公开文件保护脚本是否能识别典型误提交。检查脚本是辅助措施，不能替代人工审阅。

## 发布范围

仓库工作流只验证公开骨架，不构建、签名或发布官方客户端。也不会在 CI 中请求平台账号、下载课程或运行私有引擎。客户端资产由维护者单独准备和核验。
