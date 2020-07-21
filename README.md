# fxpki-test-tools
Some tools for generating test data, free from the fetters of mozilla-central

## What?
Mozilla have some handy tools for maintaining a set of test certificates as [part of the unit test suite for PSM](https://searchfox.org/mozilla-central/source/security/manager/ssl/tests/unit/pycert.py)

These are those tools with just enough packaging to be convenient.

## How do I use them?
It's probably best to read the instructions in the source for each script, but as a minimum:

### Setup
#### With pip
 - Find yourself a recent-ish python (I used 3.6) with pip
 - pip install the requirements like so:
 `
 pip install -r requirements.txt
 `
 - Run the tools. E.g.:
`
python pycert.py \< path/to/certspec \> path/to/pem
`

#### With virtualenv
 - Find yourself a recent-ish python (I used 3.6) with virtualenv
 - Set up a virtualenv and install the requirements like so:
 `
 ./virtualenv ./venv_fxpki
 ./venv_fxpki/bin/pip install -r requirements.txt
 `
- Run the tools within the virtuelenv, e.g.:
`
./venv_fxpki/bin/python pycert.py \< path/to/certspec \> path/to/pem
`