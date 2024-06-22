import json
import re


class Notebook:
    def __init__(self, nb_path, skip_patterns: list = None):
        code_cells = self._load_notebook_cells(nb_path)

        self.scope = {}

        if skip_patterns is None:
            skip_patterns = []

        for cell in code_cells:
            skip = False
            for pattern in skip_patterns:
                matched = re.search(pattern, cell)

                if matched is not None:
                    skip = True
                    break

            if skip:
                continue

            exec(cell, self.scope)

    def __getitem__(self, key):
        return self.scope[key]

    def _load_notebook_cells(self, nb_path):
        with open(nb_path) as f:
            raw_notebook = json.load(f)

        nb_cells = raw_notebook["cells"]

        code_cells = []

        for cell in nb_cells:
            if cell["cell_type"] == "code":
                lines = cell["source"]

                filter = lambda l: l if l[0] != '%' and l[0] != '!' else ""
                lines = [filter(line) for line in lines]

                code_cells.append("".join(lines))

        return code_cells




if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run a Jupyter notebook as a script")
    parser.add_argument("notebook", type=str, help="Path to the notebook file")
    parser.add_argument("--skip", type=str, nargs="+", help="List of patterns to skip")
    args = parser.parse_args()

    nb = Notebook(args.notebook, args.skip)
