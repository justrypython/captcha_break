#encoding:UTF-8

from setuptools import setup, find_packages

setup(
    name = 'captcha_break',
    version = '0.5',
    packages = find_packages(),
    author="Zhaoke",
    license='MIT',
    install_requires=['keras', 'tensorflow', 'opencv-python'],
    entry_points = {
        'console_scripts': [
            'captcha_break = captcha_break:load_model'
        ],
        'gui_scripts': [
            'captcha_break = captcha_break:load_model'
        ],
        'setuptools.installation': [
            'eggsecutable = captcha_break:load_model',
        ],
    },
    package_data = {
        # 任何包中含有.txt文件，都包含它
        '': ['*.h5'],
        # 包含demo包data文件夹中的 *.dat文件
        'captcha_break': ['*.png']
    }
)