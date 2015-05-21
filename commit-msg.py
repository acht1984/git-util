#! /usr/bin/env python
import sys
import re

if not re.match(r'#\d+', open(sys.argv[1]).read()):
    print('Must write issue no!')
    sys.exit(1)
