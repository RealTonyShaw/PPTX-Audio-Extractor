# PPTX 音频提取器

这个小程序可以提取 `.pptx` 幻灯片文件中的音频文件。

## 使用

安装依赖 `click`：

```shell script
pip install click
```

使用选项 `--path` 运行脚本，参数为幻灯片文件路径：

```shell script
cd Extractor
python3 entry.py --path /yourfilepath/yourfile.pptx
```

音频会被保存在目录 `/yourfilepath` 下。

## 注意

目前仅适用 `.m4a` 音频的提取。