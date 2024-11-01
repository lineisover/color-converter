$venvpath = ".venv"

. $venvpath\Scripts\activate.ps1


python -m nuitka --onefile --windows-icon-from-ico=".\assets\icon.ico" --product-name="Color Converter" --windows-company-name="DEM" --windows-product-name="Color Converter" --windows-file-version=1.0 --windows-file-description="Ex Machina Color Converter" .\src\colorconverter.py