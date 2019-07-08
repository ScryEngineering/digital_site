# digital_site

The homepage for our digital offerings

## Getting set up

Create a python virtual environment note that Gilbert currently requires Python 3.7 and that the version of setuptools is `>41.0`:

```
python3.7 -m venv venv
```

Activate the environment, on *nix

```
source venv/bin/activate
pip install -U pip
pip install -U setuptools
```

Then install requirements:
```
pip install -r requirements.txt
```