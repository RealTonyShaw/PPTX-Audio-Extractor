# PPTX-Audio-Extractor

English | [中文](README.zh-CN.md)

This gadget allows you to extract the audio files inserted into the `.pptx` powerpoint.

## Usage

Install the dependency `click`:

```shell script
pip install click
```

Run scripts with `--path` option followed by the file path:

```shell script
cd Extractor
python3 entry.py --path /yourfilepath/yourfile.pptx
```

Audios would be saved in the directory of `/yourfilepath`.

## Notice

Only the extraction of `.m4a` audios is supported currently.