from setuptools import setup
import os


this_directory = os.path.abspath(os.path.dirname(__file__))
long_description = None
total_description = None
try:
    with open(os.path.join(this_directory, 'README.md'), 'rb') as f:
        total_description = f.read().decode('utf-8')
    description_lines = total_description.split('\n')
    long_description_lines = []
    for line in description_lines:
        if not line.startswith("<meta ") and not line.startswith("<link "):
            long_description_lines.append(line)
    long_description = "\n".join(long_description_lines)
except IOError:
    long_description = 'The complete web automation library.'

setup(
    name='sb-examples',
    version='0.1.0',
    description='Examples of SeleniumBase',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/seleniumbase/SeleniumBase',
    platforms=["Windows", "Linux", "Mac OS-X"],
    author='Michael Mintz',
    maintainer='Michael Mintz',
    license="MIT",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Acceptance",
        "Topic :: Software Development :: Testing :: Traffic Generation",
        "Topic :: Utilities",
    ],
    python_requires='>=3.6',
    install_requires=[
        'seleniumbase>=4.3.2',
        'sbvirtualdisplay>=1.1.0',
        ],
    packages=[
        ],
    entry_points={
        'nose.plugins': [
            ],
        'pytest11': [
            ]
        }
    )

print("\n*** SeleniumBase Installation Complete! ***\n")
