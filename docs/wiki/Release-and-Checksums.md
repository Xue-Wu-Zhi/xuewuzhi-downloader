# 版本、Release 与文件校验


## 两个版本分别表示什么

| 版本 | 对应内容 |
| --- | --- |
| 官方客户端 V2.19.54 | 2026-10-03 的 Windows 发布包 |
| 公开骨架 0.1.0 | 本仓库的 Python 示例和公开文档 |

客户端版本与骨架版本独立。为客户端建立同名 Release 标签，不代表该标签的仓库源码能够构建出官方客户端。

## 正确获取文件

从 [Releases](https://github.com/Xue-Wu-Zhi/xuewuzhi-downloader/releases/latest) 下载 `xuewuzhi-downloader-2.19.54-windows.exe` 和 `SHA256SUMS.txt`。GitHub 自动提供的源代码压缩包只对应公开仓库。

## 校验流程

1. 使用 PowerShell 的 `Get-FileHash -Algorithm SHA256` 计算实际下载文件。
2. 与同一版本 `SHA256SUMS.txt` 中对应文件名的值比较。
3. 使用文件属性中的数字签名，或 `Get-AuthenticodeSignature`，核对发布者。

SHA-256 可以发现文件内容是否与发布记录一致；数字签名用于核对签名状态和发布者。校验值应从可信发布页面获取，不能仅比较一个来历不明的文件和它附带的校验文本。

## 当前版本记录

V2.19.54 的公开变更摘要为“完善万能下载与播放恢复”。完整资产名称、体积与哈希见[该版本说明](../releases/v2.19.54.md)。

若校验不一致，重新检查版本和下载来源，并重新下载。不要把校验失败解释为可以忽略的普通提示。
