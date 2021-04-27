font = CurrentFont()

for glyph in font:
	if glyph.lib:
		try:
			if glyph.lib['com.schriftgestaltung.Glyphs.leftMetricsKey']:
				print (glyph.name, 'L', glyph.lib['com.schriftgestaltung.Glyphs.leftMetricsKey'] )
				del glyph.lib['com.schriftgestaltung.Glyphs.leftMetricsKey']
		except:
			pass
		try:
			if glyph.lib['com.schriftgestaltung.Glyphs.rightMetricsKey']:
				print (glyph.name, 'R', glyph.lib['com.schriftgestaltung.Glyphs.rightMetricsKey'] )
				del glyph.lib['com.schriftgestaltung.Glyphs.rightMetricsKey']
		except:
			pass 
print ('NO MORE RULES')