#!C:\Users\ovidi\Desktop\Learning\PythonCourse\python_course\python_apps\App6_Mobile_App_Development_Feel_Good_App\env\Scripts\python.exe

# Author:
# Contact: grubert@users.sf.net
# Copyright: This module has been placed in the public domain.

"""
man.py
======

This module provides a simple command line interface that uses the
man page writer to output from ReStructuredText source.
"""

import locale
try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description
from docutils.writers import manpage

description = ("Generates plain unix manual documents.  "
               + default_description)

publish_cmdline(writer=manpage.Writer(), description=description)
