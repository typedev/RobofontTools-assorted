import os
from ufo2fdk.kernFeatureWriter import KernFeatureWriter
for font in AllFonts():
    path = font.path
    kernPath = path.replace(".ufo","_kern.fea")
    w = KernFeatureWriter(font)
    output = w.write()
    k = open(kernPath, 'w')
    k.write(output)
    k.close()
    print("exporting %s %s kerning feature" % (font.info.familyName, font.info.styleName))

    fea = font.features.text
    kernpath = os.path.basename(font.path).replace('.ufo', '_kern.fea')
    if not fea:
        fea = ''
    includefea = 'include ( %s );' % kernpath
    if includefea not in fea:
        fea += '\n%s' % includefea
    font.features.text = fea
