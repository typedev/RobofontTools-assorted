# coding=utf-8
from fontParts.world import *
# from anchorsLib import *
import math, os


font = CurrentFont()




def loadGroupsFile(font, mode = 'replace'): # replace / add
	fn = font.fileName + '.groups_list.txt'
	if os.path.exists(fn):
		print ('='*60)
		print (font.info.familyName, font.info.styleName)
		print ('Loading groups from file:')
		print (fn)
		f = open(fn, mode = 'r')

		for line in f:
			line = line.strip()
			groupname = line.split('=')[0]
			content = line.split('=')[1].split(',')
			# if mode == 'replace':
			# if font.groups.has_key(groupname):
			# 	print 'add glyphs to Group', groupname
			# 	for gname in content:
			# 		if gname not in font.groups[groupname] and gname in font:
			# 			font.groups[groupname].append(gname)
			# else:
			print ('Making group', groupname)
			font.groups[groupname] = ()
			glist = []
			for gname in content:
				if gname in font:
					glist.append(gname)
			font.groups[groupname] = tuple(glist)

		f.close()
		print ('Groups loaded..')
	else:
		print ('ERROR! Group file not found')


loadGroupsFile(font)


#
# for g in sorted(struk):
# 	print g, struk[g]
