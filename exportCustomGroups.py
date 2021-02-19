# coding=utf-8
from fontParts.world import *
# from anchorsLib import *
import math, os


font = CurrentFont()
group_prefix = 'public.kern' #'@MMK'

def getGroupFileName4Save(font):
	for idx in range(0,1000):
		fn = font.fileName + '.groups_list.' + str(idx) + '.txt'
		if not os.path.exists(fn):
			return fn



def saveGroups(font, groups2save):
	print ('=' * 60)
	print (font.info.familyName, font.info.styleName)
	print ('Saving groups list to file:')
	fn = getGroupFileName4Save(font)
	print (fn)
	groupsfile = open(fn, mode = 'w')

	txt = ''
	for groupname in sorted(groups2save):
		txt += '%s=%s\n' % ( groupname, ','.join(struk[groupname]) )

	# anchtxt = '\n'.join(listofanchors)
	groupsfile.write(txt)
	groupsfile.close()
	# print txt
	print ('File saved.')





def getGroups2save(font, glyphslist):
	groups2save = {}
	for glyphname in glyphslist:
		if glyphname in font:
			for groupname, content in font.groups.items():
				if groupname.startswith(group_prefix) and glyphname in content:
					if groupname not in groups2save:
						groups2save[groupname] = font.groups[groupname]
	return groups2save

struk = getGroups2save(font, font.selection)

saveGroups(font, struk)

#
# for g in sorted(struk):
# 	print g, struk[g]
