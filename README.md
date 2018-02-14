# Kanalyser

## Synopsis

Get information about .config option types and add them to the db which will be used to generate the CSV file for Machine Learning.

## Installation

Clone the repository inside your kernel sources and then patch the Makefile :

    git clone https://github.com/TuxML/Kanalyser
    git am Kanalyser/makefile.patch
    
## Usage

Still in the root of the kernel sources, do :

    make [ARCH=<arch>] scriptconfig SCRIPT=Kanalyser/fill_types.py

All entries for that architecture and version will be added (or replace the existing ones) in the database.

If warnings about duplicate entries appear, don't worry.
    
## Acknowledgments

* [Kconfiglib](https://github.com/ulfalizer/Kconfiglib)
