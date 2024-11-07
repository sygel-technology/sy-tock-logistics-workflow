# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Picking Shipped By",
    "summary": "Assign shipper contact to stock pickings",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "Sygel, Odoo Community Association (OCA)",
    "website": "https://github.com/sygel-technology/sy-stock-logistics-workflow",
    "category": "Stock",
    "depends": ["delivery"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/stock_picking_views.xml",
        "wizard/configure_shipper_wizard_views.xml",
    ],
    "installable": True,
}
