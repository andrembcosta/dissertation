import sys
from pybtex.database.input import bibtex
import subprocess

# Get unused references
result = subprocess.run(['checkcites', '--unused', sys.argv[1]], stdout=subprocess.PIPE)
console_output = result.stdout.decode('utf-8')
unused_refs = set()
for line in console_output.splitlines():
    if line.startswith("=> "):
        unused_refs.add(line[3:])

# Parse bib data
parser = bibtex.Parser()
bib_data = parser.parse_file(sys.argv[2])

# Remove duplicate bib data
for unused_ref in unused_refs:
    del bib_data.entries[unused_ref]

# Write new bibtex
f = open(sys.argv[2]+".new.bib", "a")
f.write(bib_data.to_string('bibtex'))
f.close()
