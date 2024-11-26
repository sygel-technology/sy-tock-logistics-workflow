# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Picking Product Warn Message",
    "summary": "This module add a warning popup on stock picking",
    "version": "17.0.1.0.0",
    "category": "Stock",
    "website": "https://github.com/sygel-technology/sy-stock-logistics-workflow",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "stock",
    ],
    "data": [
        "views/product_views.xml",
        "views/stock_picking_views.xml",
    ],
}
