from setuptools import setup, find_packages


setup(
    name='mkDOCter',
    version='1.0',
    url='https://github.com/willbarton/mkDOCter',
    license='CC0',
    description='mkdocs theme based on DOCter',
    author='Will Barton',
    author_email='william.barton@cfpb.gov',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'mkDOCter = mkDOCter',
        ]
    },
    zip_safe=False
)
