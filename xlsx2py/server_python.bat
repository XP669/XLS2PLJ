@echo off
title=kttools::ktexcel

mode con cols=100 lines=46

color 2

set inDir= ./xlsxs/

set outDir= ./python_out/

echo on


python xlsx2py/xlsx2py.py %inDir% %outDir% python server
pause