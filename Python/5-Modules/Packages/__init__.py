'''__init__.py exists to clearly tell Python that this folder is meant to be a package folder, making imports safe, structured, and predictable.'''
'''Without __init__.py, Python (modern versions) can still import modules, but you lose control, structure, and initialization capability—so it's still recommended in real projects.'''
'''A namespace package is a folder that Python treats as a package even without an __init__.py file'''
'''Wherever this __init__.py is there in the folder, python will treat that folder as package folder , therefore (packages.math) becomes module for import '''