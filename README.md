[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/devmanorg/19_site_generator) 

# Encyclopedia

Generate `html` pages from `.md` files

https://john2013.github.io/19_site_generator/

# How to install

Python 3 should be already installed. Then use pip (or pip3 if there is
a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.



# How to build site

```bash
python app.py
```

`.md` files must be in `articles/<section_name>/` folder.

*Topics* and *articles* must be set in `config.json` file.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
