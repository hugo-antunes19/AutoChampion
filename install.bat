@echo off

:: Verificar se o Python está instalado
python --version
if %errorlevel% neq 0 (
    echo Python nao encontrado. Baixando e instalando Python...

    :: Baixar o instalador oficial do Python
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe -OutFile python-installer.exe"

    :: Executar o instalador do Python silenciosamente
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1

    :: Remover o instalador após a instalação
    del python-installer.exe
)

:: Verificar se o PIP está instalado
pip --version
if %errorlevel% neq 0 (
    echo PIP nao encontrado. Instalando o PIP...
    python -m ensurepip --upgrade
)

echo Instalando dependencias listadas no requirements.txt...
pip install -r requirements.txt

echo Instalacao concluida!
pause
exit
