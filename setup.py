from setuptools import setup

setup(
    name='photo_sorter',
    version='1.0.0',
    author='Edward Vella',
    author_email='hello@dwardu.com',
    url='https://www.dwardu.com',
    description='A tool that sorts photos in a dated folder structure.',
    packages = ['photo_sorter'],
    install_requires = [
        'Pillow==7.0.0'
    ],
    entry_points = {
        'console_scripts': [
            'photo_sorter = photo_sorter.__main__:main'
        ]
    }
)