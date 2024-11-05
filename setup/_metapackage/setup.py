import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-stock-logistics-workflow",
    description="Meta package for sygel-technology-sy-stock-logistics-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-picking_type_confirmation_requirement_rules>=15.0dev,<15.1dev',
        'odoo-addon-picking_very_high_priority>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_force_availability>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_report_line_product_without_internal_ref>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_show_move_lots>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
