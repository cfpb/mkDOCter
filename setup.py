from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = open('README.md', 'r').read()


setup(
    name='mkDOCter',
    version='1.0.5',
    url='https://github.com/cfpb/mkDOCter',
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
    zip_safe=False,
    classifiers=[
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'License :: Public Domain',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)
