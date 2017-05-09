from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = open('README.md', 'r').read()


setup(
    name='mkDOCter',
    version='1.0.3',
    url='https://github.com/willbarton/mkDOCter',
    license='CC0',
    description='mkdocs theme based on DOCter',
    long_description=long_description,
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
