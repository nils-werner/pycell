pycell
======

Lets you execute single ["Hydrogen code cells"](https://github.com/nteract/hydrogen#hydrogen-run-cell) from a Python script:

    print "this is cell 1"

    # %%

    print "this is cell 2"

executing it using

    pycell -c 1 script.py

will print

    this is cell 2


Documentation
-------------

* [Installation](#installation)
* [Usage](#usage)
  * [Command-line](#command-line)

Installation
------------

    pip install pycell

pycell supports Python 2.7 and 3.3+.

Usage
-----

#### Command-line ####

You can call pycell directly from the command line, using `pycell` or `python -m pycell`

    python -m pycell [options] myscript.py [args...]
    
    Options:
      -h, --help            show this help message and exit
      -c, --cell            select cell to be run, defaults to the last one


This will run the selected cell from `myscript.py`
