# 安装、升级与文件校验


## 下载哪个文件

打开 [Releases](https://github.com/Xue-Wu-Zhi/xuewuzhi-downloader/releases/latest)，下载 `xuewuzhi-downloader-2.19.54-windows.exe`，这是官方 Windows 客户端。

| 文件 | 用途 |
| --- | --- |
| `xuewuzhi-downloader-2.19.54-windows.exe` | Windows 客户端发布包 |
| `SHA256SUMS.txt` | 与发布包配套的完整性校验值 |
| GitHub 自动生成的 Source code | 公开骨架与文档，不包含完整下载器 |

官网提供[备用下载入口](https://www.xuewuzhi.cn/downloader)。当前发布包面向 Windows，不能据此认为存在 macOS 或 Linux 原生客户端。开源 Python 示例的运行环境另见[开发指南](Development.md)。

## 安装与首次启动

![选择Windows客户端发布包并校验文件的下载示意](../../assets/guides/installation.png)

*通用操作示意，使用虚构数据；不是客户端截图，具体界面以当前版本为准。* [查看大图](../../assets/guides/installation.png)

1. 将文件下载到自己能访问的目录，等待浏览器确认下载完成。
2. 可先进行下方的哈希校验，再打开文件属性中的“数字签名”检查发布者。
3. 运行发布包，按实际出现的安装或解压提示操作。
4. 启动客户端，选择一个可写的课程保存目录。长课程和板书转换需要额外临时空间。
5. 先使用一门短课程验证播放结果，再继续批量任务。

## PowerShell 校验

在下载目录打开 PowerShell：

```powershell
Get-FileHash -LiteralPath '.\xuewuzhi-downloader-2.19.54-windows.exe' -Algorithm SHA256
Get-AuthenticodeSignature -LiteralPath '.\xuewuzhi-downloader-2.19.54-windows.exe' |
    Select-Object Status, @{Name='Publisher'; Expression={$_.SignerCertificate.Subject}}
```

第一条输出应与同一 Release 的 `SHA256SUMS.txt` 一致，比较时忽略大小写。该版本检查时签名状态为 `Valid`，发布者为“杭州学无止软件有限公司”。签名和哈希回答不同的问题，详见[版本与校验](Release-and-Checksums.md)。

## 更新前后

更新前等待当前任务结束，记下课程保存位置。更新后先核对客户端版本号，再测试一个原来可以正常处理的课节。若有异常，保留脱敏错误提示并查看[排错指南](Troubleshooting.md)。

如果系统提示文件损坏或发布者无法验证，先核对下载来源和校验值。不要通过关闭系统防护来代替定位问题。
