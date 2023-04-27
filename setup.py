from distutils.core import setup
import pathlib

readme = pathlib.Path('README.md').read_text()

setup(
    name='jsonl_viz',
    version='0.1.0',
    description='Visualize JSONL files in the terminal',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Andrea Tupini',
    author_email='tupini07@hotmail.com',
    url='https://github.com/tupini07/jsonl_viz',
    packages=['jsonl_viz'],
    install_requires=[
        "rich==13.3.5",
        "fire==0.5.0",
        "keyboard==0.13.5",
    ],
    entry_points={
        'console_scripts': [
            'jsonl_viz = jsonl_viz.__main__:main'
        ]
    },
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ]
)
