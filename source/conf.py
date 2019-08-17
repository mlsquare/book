# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sys
import os
import shlex




# import sphinx_py3doc_enhanced_theme
# html_theme = "sphinx_py3doc_enhanced_theme"
# html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]

# -- Project information -----------------------------------------------------

project = '100 Problems in Democratizing AI'
copyright = '2019, Soma S Dhavala'
author = 'Soma S Dhavala'

# The full version, including alpha/beta/rc tags
release = '0.01'

# add read_the_docs theme

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.autosummary',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.spelling',
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# guzzle theme

# html_theme = "press"

# import guzzle_sphinx_theme
# html_theme_path = guzzle_sphinx_theme.html_theme_path()
# html_theme = 'guzzle_sphinx_theme'
# extensions.append("guzzle_sphinx_theme")
# html_theme_options = {
#     # Set the name of the project to appear in the sidebar
#     "project_nav_name": "Project Name",
# }

html_logo = 'logo.png'
html_favicon = 'favicon.png'

# html_theme_options = {
# 'show_powered_by': False,
# # Visible levels of the global TOC; -1 means unlimited
# "globaltoc_depth": 4,
# # If False, expand all TOC entries
# "globaltoc_collapse": False,
# # If True, show hidden TOC entries
# "globaltoc_includehidden": False
# }

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'canonical_url': '',
    'logo_only': True,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_background': '#202020',
    'vcs_pageview_mode': '',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_sidebars = {
   '**': ['globaltoc.html', 'sourcelink.html'],
   'using/windows': ['windowssidebar.html'],
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
