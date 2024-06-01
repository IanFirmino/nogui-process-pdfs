from setuptools import setup, find_packages

setup(
    name='automacao_rh_v1',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PyPDF2',
    ],
    entry_points={
        'console_scripts': [
            'run_projeto=main:help',
        ],
    },
)