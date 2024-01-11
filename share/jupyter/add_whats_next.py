import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "_ext"))

from tutorials import next

dirname = sys.argv[1]
basename = sys.argv[2]
filepath = sys.argv[3]

with open(filepath) as f:
    lines = f.readlines()

for (line_index, line) in enumerate(lines):
    if "<!-- next content -->" in line:
        replaced_line = "<ul>"
        next_content = next[os.path.join(dirname, basename)]
        assert len(next_content) > 0
        for next_text, next_link in next_content.items():
            replaced_line += f'<li><a href="{next_link}" style="text-decoration: underline;">{next_text}</a></li>'
        replaced_line += "</ul>"
        lines[line_index] = replaced_line + "\n"

with open(filepath, "w") as f:
    f.write("".join(lines))
