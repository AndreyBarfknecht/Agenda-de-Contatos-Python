@echo off
title Agenda de Contatos

:: Muda o diretorio de trabalho para a pasta do script. ESSA E A CORRECAO!
cd /d "%~dp0"

echo Iniciando a Agenda de Contatos...
echo.

python main.py

echo.
echo Programa finalizado. Pressione qualquer tecla para fechar.
pause