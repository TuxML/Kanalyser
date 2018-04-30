# Kanalyser

## Synopsis

Get information about .config option types and add them to the db which will be used to generate the CSV file for Machine Learning.

You need to run this once before generating CSVs.

## Installation

While in the kernel folder, run :

    git clone https://github.com/TuxML/Kanalyser
    git am Kanalyser/makefile.patch
    
## Usage

Run in the kernel folder :

    make [ARCH=<arch>] scriptconfig SCRIPT=Kanalyser/fill_types.py

This will replace all entries in the "Properties" table of your database with 
    
## Acknowledgments

* [Kconfiglib](https://github.com/ulfalizer/Kconfiglib)
