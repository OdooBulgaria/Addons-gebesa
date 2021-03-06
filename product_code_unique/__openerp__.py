# -*- coding: utf-8 -*-
# © <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Product Code Unique",
    "summary": "Add the unique property to default_code field",
    "version": "9.0.1.0.0",
    "category": "Product",
    "website": "https://odoo-community.org/",
    "author": "<Deysy Mascorro>, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
        "product",
    ],
    "data": [
        "views/product_view.xml"
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
