#encoding:UTF-8

from setuptools import setup, find_packages

setup(
    name = 'captcha_break',
    version = '0.5',
    package_dir = {'':'src'},
    packages = find_packages('src'),
    entry_points = {
        'setuptools.installation': [
            'eggsecutable = captcha_break'
        ]
    }
)