# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import Command, api, fields, models


class ConfigureShipperWizard(models.TransientModel):
    _name = "configure.shipper.wizard"
    _description = "Configure Shipper Wizard"

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        active_ids = self.env.context.get("active_ids")
        if active_ids:
            res["stock_picking_ids"] = [Command.set(active_ids)]
        return res

    partner_id = fields.Many2one(
        comodel_name="res.partner",
        domain="[('is_shipper', '=', True)]",
        required=True,
        string="Shipped By",
    )
    weight = fields.Float(compute="_compute_weight", digits="Stock Weight")
    stock_picking_ids = fields.Many2many(comodel_name="stock.picking", readonly=True)

    @api.depends("stock_picking_ids")
    def _compute_weight(self):
        for sel in self:
            sel.weight = sum(sel.stock_picking_ids.mapped("weight"))

    def configure_shipper(self):
        self.ensure_one()
        self.stock_picking_ids.write({"shipped_by_id": self.partner_id.id})
