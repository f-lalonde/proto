cd dist\proto\
@echo off
set P=1
IF "%~2" == "" GOTO Vide
set P=2
:Vide
.\proto.exe %1 %P%

