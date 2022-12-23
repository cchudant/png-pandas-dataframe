---
title: extract_dataframe_from_png
emoji: 🥳
colorFrom: red
colorTo: yellow
sdk: gradio
sdk_version: "3.13.2"
app_file: app.py
pinned: false
---


# png-pandas-dataframe
Recover pandas dataframe hidden in image

Based on [s373r/steganography-png-decoder](https://github.com/s373r/steganography-png-decoder).

# Prepare

```
$ git clone https://github.com/cchudant/png-pandas-dataframe
$ cd png-pandas-dataframe
$ chmod +x extract_pandas_dataframe.py
```

# Bacis usage

```
$ ./extract_pandas_dataframe.py -h
```

```
usage: extract_pandas_dataframe.py [-h] file

Prints Extract CSV from PNG file

positional arguments:
  file        an PNG image

optional arguments:
  -h, --help  show this help message and exit
```
---
```
$ ./extract_pandas_dataframe.py sample-picture.png
```
