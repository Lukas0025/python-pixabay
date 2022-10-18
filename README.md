[![issues](https://img.shields.io/github/issues/Lukas0025/python-pixabay)](https://github.com/Lukas0025/python-pixabay/issues)
[![closed issues](https://img.shields.io/github/issues-closed-raw/Lukas0025/python-pixabay)](https://github.com/Lukas0025/python-pixabay/issues)
[![size](https://img.shields.io/github/repo-size/Lukas0025/python-pixabay)](https://github.com/Lukas0025/python-pixabay/)
[![last commit](https://img.shields.io/github/last-commit/Lukas0025/python-pixabay)](https://github.com/Lukas0025/python-pixabay/)

python-pixabay (pixabay) is unofficial API client library for pixabay API (https://pixabay.com/api/docs/)

### Install from pip

```sh
pip3 install pixabay
```

### Install from source

```
git clone https://github.com/Lukas0025/python-pixabay.git
cd python-pixabay
make install
```

## Getting started

### simple example

#### download image

```python
import pixabay.core

# init pixabay API
px = pixabay.core("YOUR API KEY")

# search for space
space = px.query("space")

# get len of hits len(space)
print("{} hits".format(len(space)))

# downalod fisrt image
space[0].download("space.jpg", "largeImage")
```

#### download video
```python
import pixabay.core

# init pixabay API
px = pixabay.core("YOUR API KEY")

# search for space
space = px.queryVideo("space")

# get len of hits len(space)
print("{} hits".format(len(space)))

# downalod fisrt video
space[0].download("space.mp4", "large")
```


* [examples](https://github.com/Lukas0025/python-pixabay/tree/master/examples)
* [documentation](https://python-pixabay.readthedocs.io/en/latest/annotated.html)

## Getting help

* Issues: https://github.com/Lukas0025/python-pixabay/issues

## Reporting bugs and contributing

* Want to report a bug or request a feature? Please open [an issue](https://github.com/Lukas0025/python-pixabay/issues/new).
* Want to help us with build? Contact me

## Licensing

python-pixabay is licensed under Apache2
