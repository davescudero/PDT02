import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'Prediccion de precio de productos'
copyright = '2025, David Escudero'
author = 'David Escudero'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'myst_parser',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.graphviz',
    'sphinxcontrib.mermaid',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'furo'  # Tema moderno y limpio
html_static_path = ['_static']

# Configuración de CSS personalizado
html_css_files = [
    'custom.css',
]

# Configuración de MyST
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "tasklist",
]

# Configuración de MathJax
mathjax3_config = {
    'tex': {
        'inlineMath': [['$', '$']],
        'displayMath': [['$', '$']],
        'processEscapes': True,
        'processEnvironments': True,
        'packages': ['base', 'ams', 'noerrors', 'noundefined', 'color'],
        'macros': {
            'bold': ['{\\bf #1}', 1],
            'norm': ['{\\lVert #1 \\rVert}', 1],
            'abs': ['{\\lvert #1 \\rvert}', 1]
        }
    },
    'options': {
        'processHtmlClass': 'tex2jax_process|mathjax_process|math|output_area',
        'ignoreHtmlClass': 'tex2jax_ignore|mathjax_ignore|no-mathjax'
    },
    'loader': {
        'load': ['[tex]/ams', '[tex]/noerrors', '[tex]/noundefined', '[tex]/color']
    },
    'svg': {
        'fontCache': 'global'
    }
}

# Configuración adicional para matemáticas
numfig = True
math_number_all = False
math_eqref_format = "Ecuación {number}"
math_numfig = True

# Configuración del idioma
language = 'es'
locale_dirs = ['locale/']   # path is example but recommended
gettext_compact = False     # optional 

# Configuración adicional del tema
html_theme_options = {
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "announcement": "🚀 Documentación en desarrollo activo - Última actualización: Marzo 2024",
    "light_css_variables": {
        "font-stack": "Source Sans Pro, system-ui, -apple-system, sans-serif",
        "color-brand-primary": "#2980b9",
        "color-brand-content": "#2980b9",
        "color-background-primary": "#ffffff",
        "color-background-secondary": "#f8f9fa",
        "color-announcement-background": "#e8f4f8",
        "color-announcement-text": "#2c3e50",
    },
}

# Configuración de Graphviz
graphviz_output_format = 'svg'

# Configuración de Mermaid
mermaid_version = 'latest'
mermaid_init_js = True 