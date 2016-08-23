# mkDOCter

mkDOCter is an [MkDocs](http://www.mkdocs.org/) theme based on the
[DOCter template for Jekyll](https://github.com/ascott1/DOCter).

## Usage

Use pip to install mkDOCter. If you're using mkdocs within a 
[virtualenv](https://virtualenv.pypa.io/en/stable/), please be sure to
install mkDOCter into the same virtualenv.

```
pip install mkDOCter
```

Once installed, you can add mkDOCter to your mkdocs configuraiton file:

```
theme: mkDOCter
```

## Configuration

mkDOCter has a few config extras to customize its appearances:

```
extras:
    brand_color: "#1096CF"
    logo_url: http://xmlsoft.org/catalog.gif
    logo_alt: My Awesome Logo
```

*`brand_color`* controls the header and sidebar accent lines.

*`logo_url`* is the URL to a logo to display in the top right.

*`logo_alt`* is the alt text for the logo.

## License

The project is in the public domain, and all contributions to it will be
released as such. By submitting a pull request, you are agreeing to 
waive all rights to your contribution under the terms of the 
[CC0 Public Domain Dedication](TERMS.md).

If you contribute the open source work of others, please mark it clearly 
in your pull request.
