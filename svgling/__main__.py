from __future__ import absolute_import
import svgling.core
import sys

def main(*argv):
    if len(argv) != 2:
        print >>sys.stderr, u"Please supply a python expression describing a tree."
        return
    t = eval(argv[1])
    layout = svgling.core.TreeLayout(t, options=svgling.core.TreeOptions())
    print layout._repr_svg_()

main(*sys.argv)