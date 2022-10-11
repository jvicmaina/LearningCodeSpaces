from setuptools import setup, find_packages

install_requires = []

# Although you can use this to set install_requires, check
# if you really need this or to have them separate
# https://packaging.python.org/en/latest/discussions/install-requires-vs-requirements/#install-requires-vs-requirements-files
#with open('requirements.txt', 'r') as _f:
#    install_requires = _f.read()


setup(
    name = '',
    description = '',
    packages = find_packages(),
    author = '',
    author_email = '',
    version = '0.0.1',
    url = 'https://github.com/alfredodeza/devcontainer-python-template',
    zip_safe = False,
    install_requires=[],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
    ]
)
