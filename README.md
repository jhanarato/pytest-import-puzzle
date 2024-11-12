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
