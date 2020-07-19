# doi-arxiv-to-bibtex-refs
## An implementation of arxiv2bib and doi2bib into latex using Python


As explained in [1], the usual way of citing references in Latex could be made easier by using directly the doi (unique identifier)

Execute python script Python_libs/Split.py in order to generate a .bib reference file. Or directly call it from your Latex project (see [3])

The script browses all the .tex files contained in the directories and sub-directories. It detects the citation keys \cite{key} in DOI or arXiv id format. For each identifier, the information is retrieved and a .bib file is generated. A list of existing reference files .bib can be merged with the generated file.

As an exemple, if you use arXiv format \cite{2003.02751v2} or a doi \cite{10.1016/j.jcp.2018.10.045}, the following information will be added in the .bib file


 @article{2003.02751v2,
Author        = {Ehsan Haghighat and Maziar Raissi and Adrian Moure and Hector Gomez and Ruben Juanes},
Title         = {A deep learning framework for solution and discovery in solid mechanics},
...
} 
 
 @article{10.1016/j.jcp.2018.10.045,
	doi = {10.1016/j.jcp.2018.10.045},
	url = {https://doi.org/10.1016%2Fj.jcp.2018.10.045},
	year = 2019,
	month = {feb},
	...
} 

The arXiv format detection and retrieving uses the library arxiv2bib [2]. 

I adapted a code from [1] with some changes as :

    1. Verification for doi format
    
    2. Replacing the usual ref key by the doi so that it matches the \cite{doi}
    
    3. Proper export to bib file
    
    4. Sub folder checking for .tex files research
    
    5. arXiv id support thanks to arxiv2bib module
    
    6. Adding some comments


[1] Simplifying the management of scientific reference and citation with a minimalist DOI-BibTex-LaTeX approach, Wei Li, dx.doi.org/10.15761/CMID.1000139

[2] arxiv2bib repository package, https://pypi.org/project/arxiv2bib/ 

[3] More from my blog post https://graynaud.github.io/gh-pages/making-references-easier-in-latex/
