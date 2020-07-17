# -*- coding: utf-8 -*-
"""

Part of this code is from Wei Li (doi: 10.15761/CMID.1000139)

Addings :
    1. Check for doi format
    2. Proper export to bibi file
    3. Sub folder checking for .tex files research
    4. arXiv id support thanks to arxiv2bib module
    5. Adding some comments
    
by Gaétan Raynaud, July 2020

"""

import os
import sys, numpy

from doi2bib import pydoi2bib

# RegEx pour le test de DOI
import re

# Need arxiv2bib 
# Doc @ http://nathangrigg.github.io/arxiv2bib/
import arxiv2bib


# =============================================================================
# Configuration
# =============================================================================

# Main folder of the tex document 
directory='../'
extension = ".tex"

# Name of the generated bibtex file
bibtexfilename = directory+'sample.bib'

# In case you want to add non-DOI/arXiv refs with a classical .bib file
# It will be added to the generated bibtexfile
external_bibtexfile_references = [directory+'oldSample.bib']


# =============================================================================
# Separation dans le cas de citations mutliples
# =============================================================================

def extractcitationkey(strlist):
    temp=[]
    num=len(strlist.split(','))
    if num == 1:
        return [strlist]
    else:
        for s in strlist.split(','):
            temp.append(s.replace(' ',''))
        return temp
    
# =============================================================================
# Creation de la liste des fichiers .tex
# =============================================================================

files = []
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        if filename.lower().endswith(extension):
            str_file = dirpath+'/'+filename
            files.append(str_file.replace('\\','/')) 
            #Attention aux séparations de dossiers avec des \ au lieu de /



# =============================================================================
# Initialisation du fichier bibtex
# =============================================================================
text_complet = ''                 

# Ajout des references externes

for refsfilename in external_bibtexfile_references:
    file = open(refsfilename,'r')
    text_complet += file.read()
    text_complet += ' \n \n '
    file.close()    
    
# =============================================================================
# Parcours de l'ensemble des fichiers .tex
# =============================================================================

for f in files:
    
    citationkeylist=[]
    w=open(f)
    text=w.read()
    w.close()
    length=len(text)
    mark='cite{'
    startidx=[]
    endidx=[]
    sentence=[]
    sentencelength=[]
    
    for i in range(len(text.split(mark))-1):
        sentence.append(text.split(mark)[i])
        sentencelength.append(len(sentence[i]))
        startidx.append(sum(sentencelength)+(i+1)*5)
        
    for start in startidx:
        idxlist=[]
        for i in range(start,len(text)):
            if text[i]=='}':
                idxlist.append(i)
        endidx.append(min(idxlist))
        
    for i in range(len(startidx)):
        start=startidx[i]
        end=endidx[i]
        for citationkey in extractcitationkey(text[start:end]):
            citationkeylist.append(citationkey)
            
    citationkeylist=list(set(citationkeylist))

    
    # =============================================================================
    #     Classement
    # =============================================================================
        
    # Liste de reference provenant d'arXiv
    list_arxiv_id = []
    
    for doi in citationkeylist:
        if arxiv2bib.is_valid(doi):
            list_arxiv_id.append(doi)

    refs_arxiv = arxiv2bib.arxiv2bib(list_arxiv_id)
    list_text_refs_arxiv = [arxref.bibtex() for arxref in refs_arxiv]
    
    
    # liste de reference au format doi
    list_doi_refs = []
    doi_pattern = '(10[.][0-9]{4,}[^\s"/<>]*/[^\s"<>]+)'
    
    for doi in citationkeylist:
        if re.search(doi_pattern,doi):
            list_doi_refs.append(doi)
    
    list_text_refs_doi = [pydoi2bib(doi) for doi in list_doi_refs]
    
    
    # Ajout des references doi et arxiv au fichier texte final
    if len(list_text_refs_arxiv)>0:
        text_complet += ' \n \n ' + ' \n \n '.join(list_text_refs_arxiv) + ' \n \n '
    if len(list_text_refs_doi):
        text_complet += ' \n \n ' + ' \n \n '.join(list_text_refs_doi) + ' \n \n '


# =============================================================================
# Ecriture dans le fichier Bibtex de toutes les references trouvees        
# =============================================================================


bibtexfile = open(bibtexfilename,'w')
bibtexfile.write(text_complet)
bibtexfile.close()


print('Ok, normal end')