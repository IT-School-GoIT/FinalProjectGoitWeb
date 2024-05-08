import sys
import os

sys.path.append(os.path.abspath('../..'))
project = 'Fox.Web.Assistant'
copyright = '2024, Babenko Anton - Danil Kazakov - Vitalii Bielimov -  Daryna Mirzagholi - Valerii Yermak'
author = 'Babenko Anton - Danil Kazakov - Vitalii Bielimov -  Daryna Mirzagholi - Valerii Yermak'
release = 'Це розробка програмного забезпечення, яке включає в себе книгу контактів з можливістю збереження контактних даних, нотатки для запису текстової інформації та функцію завантаження та категоризації файлів користувача, а також зведення новин з різних джерел за обраною тематикою.'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinxcontrib_django',
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Додайте параметр django_settings
django_settings = 'root.settings'
