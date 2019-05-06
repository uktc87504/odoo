# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Clearly Nedelya',
    'category': 'Accounting',
    'description': """
This module gathers dependancies for nedelya.ro's odoo solution.
==========================================================================
Once the POS-es are defined (in Point of Sale/Configuration/Point of Sales), the Managers
can set the parameters for each PoS. Like users, POSBox address, etc.

The accountant has the possibility to see the total of amount per PoS.

Three reports are available:
----------------------------
    1. The first is 
    2. The second is 
    3. The last one is
""",
    'website': 'http://www.clearlypro.eu/erp',
    'depends': ['account'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'demo': ['data/clearly_nedelya_demo.xml'],
}
