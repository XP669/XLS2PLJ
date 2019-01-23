@echo off
title=kttools::ktexcel

mode con cols=100 lines=46

color 2

set inDir= ./xlsxs/

set outDir= ./lua_out/

echo on


python xlsx2plj/xlsx2plj.py %inDir% %outDir% lua client
pause