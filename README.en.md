<div align="center">

<img src="assets/hero.svg" alt="Xuewuzhi Downloader — organize courses for offline study." width="100%">

# Xuewuzhi Downloader

Windows course video downloader, courseware organizer and offline study companion.

**[Download for Windows](https://github.com/Xue-Wu-Zhi/xuewuzhi-downloader/releases/latest)** · **[User guides](https://github.com/Xue-Wu-Zhi/xuewuzhi-downloader/wiki)** · **[简体中文](README.md)**

</div>

Xuewuzhi Downloader (学无止下载器) is a Windows desktop client for course video downloads, lecture replay downloads, audio and courseware such as PDF or presentation attachments. It also processes supported whiteboard and multi-panel course formats for offline study. You must be authorized to access and retain the content; supported resources vary by platform and course.

**This repository contains public documentation and an independently written, runnable Python scaffold.** The production download engine, authentication system and platform adapters are not open sourced here. Download the official client from Releases to use the actual product.

## What the official client offers

- Course and chapter selection, with organized local files.
- Video, audio and course materials where the source platform provides them.
- Batch input or multi-course selection on supported entries.
- Whiteboard and multi-panel processing for supported course formats.
- Direct media links and selected HTML / URL conversion tools.
- A universal download mode, subject to the resources it can identify.

The public tutorial snapshot has **156 entries**: 151 platform-oriented guides and 5 link or conversion guides. Some entries cover different products or entry points from the same brand. This is a documentation count, not a claim of 156 independently tested services.

See the [platform index](docs/wiki/Platforms.md), [getting started](docs/wiki/Getting-Started.md) and [troubleshooting guide](docs/wiki/Troubleshooting.md). Detailed guides are currently in Chinese.

## Run the public scaffold

Python 3.9 or newer; no third-party runtime dependencies:

```bash
git clone https://github.com/Xue-Wu-Zhi/xuewuzhi-downloader.git
cd xuewuzhi-downloader
python -m xuewuzhi_downloader demo
python -m xuewuzhi_downloader platforms --query MOOC
```

The demo prints a fictional course tree. It does not contact a platform, read credentials or download files. The abstract interfaces are educational examples, not the official client's plugin API.

## Releases and licensing

The current official Windows release is **V2.19.56**, dated **2026-10-07**. The public scaffold is version **0.1.0**. Download `xuewuzhi-downloader-2.19.56-windows.exe` from [Releases](https://github.com/Xue-Wu-Zhi/xuewuzhi-downloader/releases/latest); the automatically generated source archives contain only this public repository.

Public code and documentation use the [MIT License](LICENSE). The official client binaries and their third-party components have separate terms; see [NOTICE](NOTICE.md). Only save content you have permission to access and retain.

Contributions to documentation, public metadata and offline examples are welcome. Read [CONTRIBUTING](CONTRIBUTING.md) and avoid submitting personal account data or proprietary implementations.
