{
    'name': 'Airproof Theme',
    'description': 'Thème airproof',
    'category': 'Website/Theme',
    'version': '1.0',
    'author': 'Ingenosya',
    'depends': ['base', 'website','website_sale'],
    'data': [
        'views/website_templates.xml',  # Vue personnalisée de l'en-tête
        'data/presets.xml',  # Ajout de l'option dans l'éditeur de site
        'data/pages/404.xml',
        'data/pages/home.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            'website_airproof/static/src/scss/primary_variables.scss',

        ],
        'web.assets_frontend': [
            'website_airproof/static/src/scss/main.scss',
            'website_airproof/static/src/scss/header.scss',
            'website_airproof/static/src/js/website.js',
        ],
    },
    'icon': '/website_airproof/static/description/logo.png',
    'installable': True,
    'application': True,
    'auto_install': False,
}
