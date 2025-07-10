@echo off
title Instalador de Dependencias - Agenda de Contatos
echo.
echo ==============================================================
echo    Este script vai instalar as bibliotecas necessarias
echo    para a Agenda de Contatos funcionar.
echo ==============================================================
echo.
echo Verificando se o PIP (gerenciador de pacotes do Python) esta disponivel...
echo.

pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: O comando 'pip' nao foi encontrado.
    echo Verifique se o Python foi instalado corretamente no seu computador.
    echo Lembre-se de marcar a opcao "Add Python to PATH" durante a instalacao.
    echo.
    pause
    exit /b
)

echo Iniciando a instalacao da biblioteca 'pyfiglet'...
echo.
pip install -r requirements.txt

echo.
echo ==============================================================
echo    Instalacao concluida com sucesso!
echo ==============================================================
echo.
echo Voce ja pode fechar esta janela e executar o programa
echo clicando no arquivo 'executar.bat'.
echo.
pause