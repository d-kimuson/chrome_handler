from setuptools import setup, find_packages

readme = './README.md'
license = './LICENSE'

setup(
    name='chrome_handler',
    version='0.0.1',
    description='Handling chrome driver with selenium.',
    long_description=readme,
    author='Kaito Kimura',
    author_email='mail.kaito03@gmail.com',
    install_requires=['beautifulsoup4==4.9.1', 'selenium==3.141.0'],
    url='https://github.com/kaito1002/chrome_handler',
    license=license,
    packages=find_packages()
)
