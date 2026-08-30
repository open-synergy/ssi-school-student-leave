import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-school-student-leave",
    description="Meta package for open-synergy-ssi-school-student-leave Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_school_student_leave',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
