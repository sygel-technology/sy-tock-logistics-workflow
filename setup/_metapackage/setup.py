import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-sygel-technology-sy-stock-logistics-workflow",
    description="Meta package for sygel-technology-sy-stock-logistics-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-picking_serial_list',
        'odoo14-addon-picking_very_high_priority',
        'odoo14-addon-stock_manual_shipping_weight',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
