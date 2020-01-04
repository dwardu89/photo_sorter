import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='photo_sorter',
    version='1.0.0',
    author='Edward Vella',
    author_email='hello@dwardu.com',
    url='https://github.com/dwardu89/photo_sorter',
    description='A tool that sorts photos in a dated folder structure.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages = setuptools.find_packages(),
    install_requires = [
        'Pillow==7.0.0'
    ],
    entry_points = {
        'console_scripts': [
            'photo_sorter = photo_sorter.__main__:main'
        ]
    }
)