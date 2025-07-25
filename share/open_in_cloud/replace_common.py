import os
import sys

import nbformat

branch = sys.argv[1]

for filepath in sys.argv[2:]:
    dirpath = os.path.dirname(filepath)
    with open(filepath) as f:
        nb = nbformat.read(f, as_version=4)

    for cell in nb.cells:
        if cell.cell_type == "code":
            if cell.source.startswith("import common"):
                lines = cell.source.splitlines()
                assert len(lines) == 1
                import_call, _ = lines[0].split("#")  # discard lint comment
                number_backend = import_call.strip().replace(
                    "import common_", "").strip().replace("as common", "").strip()
                number, backend = number_backend.split("_")
                assert number in ("01", "03")
                assert backend in ("dolfinx", "firedrake")
                download = (
                    f"!wget https://github.com/viskex/viskex/raw/{branch}/{dirpath}/common_{number}_{backend}.py")
                if number == "03":
                    download = (
                        f"!wget https://github.com/viskex/viskex/raw/{branch}/{dirpath}/common_{number}_none.py\n"
                        f"    {download}"
                    )
                cell.source = f"""try:
    import common_{number}_{backend} as common
except ImportError:
    {download}
    import common_{number}_{backend} as common"""

    with open(filepath, "w") as f:
        nbformat.write(nb, f)
