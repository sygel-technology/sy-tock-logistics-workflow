# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    is_shipped = fields.Boolean()
    shipped_by_id = fields.Many2one(
        comodel_name="res.partner",
        domain="[('is_shipper', '=', True)]",
        string="Shipped By",
    )
