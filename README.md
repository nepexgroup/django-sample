Example to create reusable software in python (Django)

```
python setup.py sdist
python -m pip install --user django-polls/dist/sample-0.1.tar.gz
python -m pip uninstall sample
```
