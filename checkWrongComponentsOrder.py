count = 0
for glyph in CurrentFont():
	if glyph.components:
		for font in AllFonts():
			glyphB = font[glyph.name]
			for idx, component in enumerate(glyph.components):
				if component.baseGlyph != glyphB.components[idx].baseGlyph:
					print('wrong components order -', glyph.name)
					print('-', glyph.font.info.styleName)
					for component in glyph.components:
						print ('\t',component.baseGlyph)
					print('-', glyphB.font.info.styleName)
					for component in glyphB.components:
						print ('\t',component.baseGlyph) 
					count+=1

print('total', count)

			