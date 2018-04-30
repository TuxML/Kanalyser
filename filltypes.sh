cd ..
patch -p1 <  Kanalyser/makefile.patch
make scriptconfig SCRIPT=Kanalyser/filltypes.py
