roundAndKill = True
for font in AllFonts():
	pairs2kill = []
	countrounded = 0
	print ('\n++++++++++++++++++++++++++++++++++++++++')
	print (font.info.familyName, font.info.styleName)
	print ('total:\t', len(font.kerning.items()))
	for (l,r),v in font.kerning.items():
		if abs(int(round(v,0))) < 6:
			v = 0
		v = int(round(int(round(v/5.0)*5.0),0))
		if v != 0:
			countrounded +=1
			if roundAndKill:
				font.kerning[(l,r)] = v
		else:
			pairs2kill.append((l,r))
	for pair in pairs2kill:
		if roundAndKill:
			font.kerning.remove(pair)

	print ('2round:\t', countrounded)
	print ('2kill:\t', len(pairs2kill))
	print ('result:\t', len(font.kerning.items()))
			
			
	