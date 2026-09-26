#!/usr/bin/env python3
"""Inline tools/assets.json into tools/royal-rush.src.html -> royal-rush.html + index.html (single self-contained file)."""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, 'royal-rush.src.html')).read()
assets = open(os.path.join(here, 'assets.json')).read()
json.loads(assets)
out = src.replace('/*__ASSETS__*/', 'const ASSETS=' + assets + ';')
for name in ('royal-rush.html', 'index.html'):
    dst = os.path.join(here, '..', name)
    open(dst, 'w').write(out)
    print('wrote', os.path.normpath(dst), f'{len(out.encode())/1024/1024:.2f} MB')
