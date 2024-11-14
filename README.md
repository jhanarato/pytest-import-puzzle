# A minimal example of an import problem

In the project https://github.com/jhanarato/leaftracker-gtk I'm getting an exception when running pytest within a flatpak:

```
_______________________ ERROR collecting test_example.py _______________________
ImportError while importing test module '/app/share/leaftracker-gtk/leaftracker_gtk_tests/test_example.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
test_example.py:1: in <module>
    from main import main
../leaftracker_gtk/main.py:27: in <module>
    from .main_window import MainWindow
E   ImportError: attempted relative import with no known parent package
```

It's been tricky to fix, so this project is a mimimal implementation to demonstrate and solve the problem.

# Install & Run

In the project root run the following, after setting up a virtual environment.

```commandline
pip install -r requirements.txt
pytest
```

# Notes

- The code in `src/` probably doesn't need that `__init__.py`, but removing it doesn't fix the problem.

# Solution

As it turns out, Flatpak copies the source files into the directory `leaftracker_gtk`. When running the application as configured in `leaftracker-gtk.in` that directory is used as a package. In the code in this project we run the source as it is, so relative imports don't work.
