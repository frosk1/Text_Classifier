Text_Classifier
=============

GitHub: https://github.com/frosky/Text_Classifier


About
=====

This text classification system was build in the course of the Bachelorarbeit
"Entwicklung eines schwach überwachten Modells zur Bewertung von automatisch
generierten Texten" from Jan Wessling. The system classifies textpair objects
from a developed corpus. A textpair was annotated by the text quaility of its
inner text objects. A classification tries to predict the highly subjective choice
of Text quality. The system is able to deal with different data structures
to ensure an easy to use classification mechanism. All classification
algorithms are part of the scikit-learn python modul.

See reference : https://github.com/scikit-learn/scikit-learn

Requirements-Python
============
-  Python 2.7.x 
-  Numpy 1.9.2
-  Scipy 0.14.1
-  scikit-learn 0.17
-  nltk 3.1 
-  pyphen 0.9.2

Other Requirements
============
POS-Tagger from Helmut Schmid(1994) : http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/data/tree-tagger1.pdf

Dependency-Parser from Sennrich et al.(2009) : https://files.ifi.uzh.ch/CL/volk/papers/Sennrich_Schneider_Volk_Warin_Pro3Gres_GSCL.pdf



-  ParZu - Dependency Parser : https://github.com/rsennrich/parzu
-  Treetagger ; Helmut Schmid http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/
-  treetaggerwrapper for python ; http://treetaggerwrapper.readthedocs.org/en/latest/

Use System
============
First change the needed file paths in main.py and ressource_path.py. After that your whole system is build in main()
of the main.py.

Use the classification system in the main method.

-  Set Korpus
-  Set Data
-  Attach Features
-  Set Model
-  Start Classification with Report
