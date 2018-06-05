PROIT Fee
=========

## Installation ##

Need use Python version more than 3.4.

Steps:

* sudo apt-get install libxml2-dev libxslt1-dev python3-pip
* pip3 install $(cat ./requires.txt)

## Execution ##

    python3 -m fee


## ENV variables ##

To see files .env

    PYTHON_BIN_FILE - (by default: python3)
    PROIT_FEE_STAT_URL - (by default: no)
    PROIT_FEE_STAT_KEY - (by default: no)
    PROIT_FEE_STAT_PERCENT_URL - (by default: no)
    PROIT_FEE_YEAR - (by default: current year)
    PROIT_FEE_PERCENT - (by default: 1.0)
    PROIT_FEE_FILE - (by default: path on server)
