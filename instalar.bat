@echo off
title Instalador de Dependencias - Agenda de Contatos

:: Muda o diretorio de trabalho para a pasta do script. ESSA E A CORRECAO!
cd /d "%~dp0"

echo.
echo ==============================================================
echo    Este script vai instalar as bibliotecas necessarias
echo    para a Agenda de Contatos funcionar.
echo ==============================================================
echo.

if not exist "requirements.txt" (
    echo ERRO: O arquivo 'requirements.txt' nao foi encontrado nesta pasta.
    echo Certifique-se de que ele esta no mesmo local que este script.
    pause
    exit /b
)

echo Iniciando a instalacao das bibliotecas...
echo.
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ==============================================================
    echo    ERRO DURANTE A INSTALACAO!
    echo ==============================================================
    echo Nao foi possivel instalar as bibliotecas. Verifique as
    echo mensagens de erro acima.
    echo.
    pause
    exit /b
)

echo.
echo ==============================================================
echo    Instalacao concluida com sucesso!
echo ==============================================================
echo.
echo Voce ja pode fechar esta janela e executar o programa
echo clicando no arquivo 'executar.bat'.
echo.
pause