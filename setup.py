from setuptools import setup, find_packages

setup(
    name='quiver_engine',
    version="0.1.4.1.4",
    author="Jake Bian",
    author_email="jake@keplr.io",
    description=("Interactive per-layer visualization for convents in keras"),
    license='mit',
    packages=find_packages(),
    include_package_data=True,
    package_dir={'quiver_engine': 'quiver_engine'},
    package_data={'quiver_engine': ['quiverboard/dist/*']},
    install_requires=[
        'keras',
        'tensorflow',
        'flask',
        'flask_cors',
        'gevent',
        'numpy',
        'pillow'
    ]
)
