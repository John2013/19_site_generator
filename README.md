# Encyclopedia

Site showing `.md` files as `html` pages

https://devmanopedia.herokuapp.com/

# How to install

Python 3 should be already installed. Then use pip (or pip3 if there is
a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

`.md` files must be in `articles/<section_name>/` folder.

*Section names* and *articles names* must be named like `<sort_number>_<name>`


# How to run local server

```bash
python app.py
```

Then open http://127.0.0.1:5000


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
