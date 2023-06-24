from setuptools import setup, find_packages

setup(
    name='dragonizer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Hier können Abhängigkeiten hinzugefügt werden
    ],
    entry_points={
        'console_scripts': [
            'dragonizer=dragonizer:main',
        ],
    },
)
