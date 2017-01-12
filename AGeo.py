#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import ui.main as mainWindow
import ui.start as mainDialog
import ui.mainMasopust as mainWindowMasopust
from PySide import QtGui, QtSql, QtCore
import createDB
import site
import mainWindow as m
import mainWindowMasopust as mas
import pickle
import subprocess
import os.path
import re
from xml.etree import ElementTree as ET

import numpy as np

import matplotlib
import matplotlib.pyplot as plt

# data_path = os.getcwd() + '/AGeo'
# sys.path.insert(0, data_path + '/data.zip')
# os.chdir(data_path)

from main import main

main()
