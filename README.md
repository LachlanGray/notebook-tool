Little thing for getting at stuff inside jupyter notebooks.

Executes the cells of a jupyter notebook in order, skips cells that match any skip patterns, variable states can then be accessed as keys:
```
nb = Notebook("test_nb.ipynb", skip_patterns=["DontRunThisCell"])

print(nb['x'])
```

Also runs as a script
```
python notebook.py test_nb.ipynb --skip DontRunThisCell
```
