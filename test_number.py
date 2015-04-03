#!/usr/bin/python

import sys, os
sys.path.insert(0, os.getcwd())

import secret_repo.number

assert secret_repo.number.NUMBER == 42
