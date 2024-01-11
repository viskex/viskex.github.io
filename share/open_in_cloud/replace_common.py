import os
import sys

import nbformat

branch = sys.argv[1]

for filepath in sys.argv[2:]:
    with open(filepath) as f:
        nb = nbformat.read(f, as_version=4)

    for cell in nb.cells:
        if cell.cell_type == "code":
            if cell.source.startswith("import common"):
                lines = cell.source.splitlines()
                assert len(lines) == 1
                import_call, _ = lines[0].split("#")  # discard lint comment
                backend = import_call.strip().replace("import common_", "").strip().replace("as common", "").strip()
                assert backend in ("dolfinx", "firedrake")
                cell.source = f"""try:
    import common_{backend} as common
except ImportError:
    !wget https://github.com/viskex/viskex/raw/{branch}/{os.path.dirname(filepath)}/common_{backend}.py
    import common_{backend} as common"""

    with open(filepath, "w") as f:
        nbformat.write(nb, f)
