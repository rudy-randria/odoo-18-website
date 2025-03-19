{
    'name': 'odoo-18-website',
    'description': 'Site odoo 18',
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
            'odoo-18-website/static/src/scss/primary_variables.scss',

        ],
        'web.assets_frontend': [
            'odoo-18-website/static/src/scss/main.scss',
            'odoo-18-website/static/src/scss/header.scss',
            'odoo-18-website/static/src/scss/home.scss',
            'odoo-18-website/static/src/js/website.js',
        ],
    },
    'icon': '/odoo-18-website/static/description/logo.png',
    'installable': True,
    'application': True,
    'auto_install': False,
}
