# png-pandas-dataframe
Recover pandas dataframe hidden in image

Based on [s373r/steganography-png-decoder](https://github.com/s373r/steganography-png-decoder).

# Prepare

```
$ git clone https://github.com/cchudant/png-pandas-dataframe
$ cd png-pandas-dataframe
$ chmod +x png-pandas-dataframe.py
```

# Bacis usage

```
$ ./png-pandas-dataframe.py -h
```

```
usage: png-pandas-dataframe.py [-h] file

Prints PNG text sections

positional arguments:
  file        an PNG image

optional arguments:
  -h, --help  show this help message and exit
```
---
```
$ ./png-pandas-dataframe.py sample-picture.png
```
