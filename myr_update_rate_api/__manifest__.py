# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Update tipo de cambio masivo desde api',
    'icon': '/l10n_pe/static/description/icon.png',
    'version': '0.1',
    'summary': 'Tipo de Campo',
    'category': 'Accounting/Localizations/EDI',
    'author': 'MYR Consultoria en Sistemas SAC',
    'license': 'OEEL-1',
'description': """
EDI Peru Localization

    """,
    'depends': [
        'l10n_pe_edi',
    ],
    
    "data": [
        'views/form_view.xml',
    ],
    
    'installable': True,
}
