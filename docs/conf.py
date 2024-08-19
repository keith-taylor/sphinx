# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Serenity'
author = 'Keith Taylor'

from datetime import datetime
year = datetime.now().year
if year > 2024:
	copyright = f'2024-{year}, {author}'
else:
	copyright = f'2024, {author}'

import importlib.util
import os

# import the module
spec = importlib.util.spec_from_file_location("serenity", os.path.abspath('../src/__init__.py'))
serenity = importlib.util.module_from_spec(spec)
spec.loader.exec_module(serenity)

release = serenity.__version__


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx_new_tab_link']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
