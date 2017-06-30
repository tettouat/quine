#!/usr/bin/python
import os
fichier = open("Grace_kid.py", "w+")
"""
commentaire
"""
s = '#!/usr/bin/python\nimport os\nfichier = open("Grace_kid.py", "w+")\n"""\ncommentaire\n"""\ns = %r\nfichier.write(s%%s)\nfichier.close()\nos.chmod("Grace_kid.py", 0755)\n'
fichier.write(s%s)
fichier.close()
os.chmod("Grace_kid.py", 0755)
