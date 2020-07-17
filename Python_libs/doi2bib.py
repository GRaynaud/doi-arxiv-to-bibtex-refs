# -*- coding: utf-8 -*-
"""
Python Code from 
Simplifying the management of scientific reference and citation with a minimalist DOI-BibTex-LaTeX approach

author : Wei Li
Addings by Gaétan Raynaud

Reference : doi: 10.15761/CMID.1000139

"""

import os
import sys, numpy
import re

from six.moves import urllib
from urllib.request import Request
from urllib.request import urlopen

def pydoi2bib(doi):
    completeURL='https://doi.org/' + doi
    q = Request(completeURL)
    q.add_header('Accept', 'application/x-bibtex; charset=utf-8')
    a = urlopen(q).read()
    a_decode = a.decode('utf-8')
    # Need to change the reference key to the actual doi
    
    regexp = r'@([a-z]*){[a-zA-Z0-9_-]*,'
    repl = r'@\1{'+doi+','
    a_modif = re.sub(regexp,repl,a_decode)
    return a_modif

if '__name__' == '__main__':
    doi='10.1172/jci27167'
    print(pydoi2bib(doi))
    doi='10.1088/1361-6501/aa8c1c'
    print(pydoi2bib(doi))
    doi = '10.15761/CMID.1000139'
