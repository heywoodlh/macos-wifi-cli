from setuptools import setup
import sys


def readme():
    with open('README.md') as f:
        return f.read()

if sys.platform == "darwin":
    setup(name='macos-wifi-cli',
          version='0.1.0',
          description="MacOS Wifi CLI client",
          long_description=readme(),
          long_description_content_type='text/markdown',
          classifiers=[
              "Intended Audience :: Developers",
              "Operating System :: MacOS"
              ],
          url='https://github.com/heywoodlh/macos-wifi-cli',
          author='Spencer Heywood',
          author_email='l.spencer.heywood@protonmail.com',
          license='APACHE-2.0',
          packages=['macos-wifi-cli'],
          scripts=['bin/wifi'],
          python_requires='>3.5.2',
          zip_safe=False)
else:
    print("Operating system unsupported! Exiting.")
    sys.exit(1)
