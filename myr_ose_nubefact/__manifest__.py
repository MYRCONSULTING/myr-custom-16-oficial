# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Nubefact - EDI for Peru',
    'icon': '/l10n_pe/static/description/icon.png',
    'version': '0.1',
    'summary': 'Electronic Invoicing for Peru (OSE method) and UBL 2.1',
    'category': 'Accounting/Localizations/EDI',
    'author': 'MYR Consultoria en Sistemas SAC',
    'license': 'OEEL-1',
'description': """
EDI Peru Localization
======================
Allow the user to generate the EDI document for Peruvian invoicing.

By default, the system uses the IAP proxy.  This has the advantage that you
can use the system immediately the moment you choose Nubefact as your OSE
in the SUNAT portal.

You can also directly send it to Nubefact if you bought an account from them
and even to SUNAT in case of contingency.

We support sending and cancelling of customer invoices.
    """,
    'depends': [
        #'iap',
        #'l10n_pe',
        #'product_unspsc',
        #'account_edi',
        'l10n_pe_edi',
    ],
    #'auto_install': ['l10n_pe', 'account_edi'],
    "data": [
        'views/res_config_nubefact.xml',
    ],
    
    'external_dependencies': {
        'python': ['pyOpenSSL']
    },
    
    'installable': True,
}
