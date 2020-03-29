from setuptools import setup, find_packages


with open('README.md', 'r') as r_file:
    long_description = r_file.read()

setup(
    name='file-watcher',
    version='0.1.0',
    author='Ilya Biryukov',
    author_email='biryukovsky@gmail.com',
    description='File watcher',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.6',
    entry_points={'console_scripts': 'watch = watcher.run:main'},
)
