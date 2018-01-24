# Kanalyser

## Synopsis

Gets all possible values for linux kernel config options in the context of Machine Learning data input for the TuxML Project.

## Installation

Clone the repository inside your kernel sources and then patch the Makefile :

    git clone https://github.com/TuxML/Kanalyser
    git am Kanalyser/makefile.patch
    
## Usage

    make [ARCH=<arch>] PYTHONCMD=python3 scriptconfig SCRIPT=Kanalyser/<script>.py [SCRIPT_ARG=<arg>]
    
## Acknowledgments

* [Kconfiglib](https://github.com/ulfalizer/Kconfiglib)
