import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='photo-org',
    version=open("version", "r").read(),
    author='Edward Vella',
    author_email='hello@dwardu.com',
    url='https://github.com/dwardu89/photo_sorter',
    description='A tool that sorts photos in a dated folder structure.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    packages = setuptools.find_packages(),
    install_requires=[
            "exifread", "Pillow", "colorama"
        ],
    include_package_data=True,
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'photo_sorter = photo_sorter.__main__:main'
        ]
    }
)
