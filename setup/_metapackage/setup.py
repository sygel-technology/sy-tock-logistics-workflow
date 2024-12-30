import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-stock-logistics-workflow",
    description="Meta package for sygel-technology-sy-stock-logistics-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-picking_carrier_tracking_ref_search>=16.0dev,<16.1dev',
        'odoo-addon-picking_edit_printed_status>=16.0dev,<16.1dev',
        'odoo-addon-product_search_category_attribute_stock>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_terms>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
