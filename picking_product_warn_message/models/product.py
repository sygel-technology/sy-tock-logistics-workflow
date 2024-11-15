# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    out_picking_line_warn_message = fields.Text(string="'Message for Out Pickings'")
    in_picking_line_warn_message = fields.Text(string="'Message for In Pickings'")
