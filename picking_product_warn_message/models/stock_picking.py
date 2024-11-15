# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    in_picking_product_warn_msg = fields.Html(
        compute="_compute_in_picking_product_warn_msg"
    )
    out_picking_product_warn_msg = fields.Html(
        compute="_compute_out_picking_product_warn_msg"
    )

    def _compute_in_picking_product_warn_msg(self):
        for rec in self:
            in_picking_product_warn_msg = ""
            separator = "<br/>"
            if rec.picking_type_code in ["incoming"] and rec.move_ids_without_package:
                warnable_products = rec.move_ids_without_package.mapped(
                    "product_id"
                ).filtered(lambda p: p.in_picking_line_warn_message)
                in_picking_product_warn_msg = separator.join(
                    [
                        f"<b>{product_id.display_name}: </b>"
                        f"<span>{product_id.in_picking_line_warn_message}</span>"
                        for product_id in warnable_products
                    ]
                )
            rec.in_picking_product_warn_msg = in_picking_product_warn_msg

    def _compute_out_picking_product_warn_msg(self):
        for rec in self:
            out_picking_product_warn_msg = ""
            separator = "<br/>"
            if rec.picking_type_code in ["outgoing"] and rec.move_ids_without_package:
                warnable_products = rec.move_ids_without_package.mapped(
                    "product_id"
                ).filtered(lambda p: p.out_picking_line_warn_message)
                out_picking_product_warn_msg = separator.join(
                    [
                        f"<b>{product_id.display_name}: </b>"
                        f"<span>{product_id.out_picking_line_warn_message}</span>"
                        for product_id in warnable_products
                    ]
                )
            rec.out_picking_product_warn_msg = out_picking_product_warn_msg
