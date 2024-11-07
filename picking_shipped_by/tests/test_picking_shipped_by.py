# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo.tests.common import TransactionCase


class TestPickingShippedBy(TransactionCase):
    def setUp(cls):
        super().setUp()
        cls.partner_1 = cls.env["res.partner"].create({"name": "Partner-1"})
        cls.partner_2 = cls.env["res.partner"].create({"name": "Partner-2"})
        cls.shipper = cls.env["res.partner"].create(
            {"name": "Shipper", "is_shipper": True}
        )
        cls.picking_1 = cls.env["stock.picking"].create(
            {
                "location_id": cls.env.ref("stock.stock_location_stock").id,
                "location_dest_id": cls.env.ref("stock.stock_location_customers").id,
                "partner_id": cls.partner_1.id,
                "picking_type_id": cls.env.ref("stock.picking_type_out").id,
            }
        )
        cls.picking_2 = cls.env["stock.picking"].create(
            {
                "location_id": cls.env.ref("stock.stock_location_stock").id,
                "location_dest_id": cls.env.ref("stock.stock_location_customers").id,
                "partner_id": cls.partner_2.id,
                "picking_type_id": cls.env.ref("stock.picking_type_out").id,
            }
        )

    def test_configre_shipper(self):
        self.assertFalse(self.picking_1.shipped_by_id)
        self.assertFalse(self.picking_2.shipped_by_id)
        context = {
            "active_ids": [self.picking_1.id, self.picking_2.id],
            "active_model": "stock.picking",
        }
        wizard = (
            self.env["configure.shipper.wizard"]
            .with_context(**context)
            .create({"partner_id": self.shipper.id})
        )
        wizard.partner_id = self.shipper.id
        wizard.configure_shipper()
        self.assertEqual(self.picking_1.shipped_by_id, self.shipper)
        self.assertEqual(self.picking_2.shipped_by_id, self.shipper)
