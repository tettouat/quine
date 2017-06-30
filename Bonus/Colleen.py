#!/usr/bin/python
def disp(functionBody):
	print "#!/usr/bin/python"
	print "def disp(functionBody):"
	print functionBody
	print "'''"
	print "commentaire_hors_main"
	print "'''"
	print "def main():"
	print "\t'''"
	print "\tcommentaire_main"
	print "\t'''"
	print "\tdisp(" + repr(functionBody) + ")"
	print "main()"
'''
commentaire_hors_main
'''
def main():
	'''
	commentaire_main
	'''
	disp('\tprint "#!/usr/bin/python"\n\tprint "def disp(functionBody):"\n\tprint functionBody\n\tprint "\'\'\'"\n\tprint "commentaire_hors_main"\n\tprint "\'\'\'"\n\tprint "def main():"\n\tprint "\\t\'\'\'"\n\tprint "\\tcommentaire_main"\n\tprint "\\t\'\'\'"\n\tprint "\\tdisp(" + repr(functionBody) + ")"\n\tprint "main()"')
main()
