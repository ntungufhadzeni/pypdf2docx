from setuptools import setup

setup(
    name='pypdf2docx',
    version='0.0.1',
    install_requires=["pdf2docx==0.5.6"],
    packages=['pypdf2docx'],
    entry_points={
        'console_scripts': [
            'pypdf2docx = pypdf2docx.pypdf2docx:main',
        ]
    }
    
)