from distutils.core import setup
import pathlib

requirements = pathlib.Path('requirements.txt').read_text().splitlines()
requirements = [r for r in requirements
                if not r.startswith('#')
                and not r.strip() == ""]

readme = pathlib.Path('README.md').read_text()

setup(
    name='jsonl_viz',
    version='1.0.0',
    description='Visualize JSONL files in the terminal',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Andrea Tupini',
    author_email='tupini07 AT hotmail DOT com',
    url='https://github.com/tupini07/jsonl_viz',
    packages=['jsonl_viz'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'jsonl_viz = jsonl_viz.__main__:main'
        ]
    }
)
