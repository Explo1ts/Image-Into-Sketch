@echo off
echo ============================================
echo   Installing required Python dependencies...
echo ============================================

:: Upgrade pip first
python -m pip install --upgrade pip

:: Install required packages
pip install --upgrade pip
pip install opencv-python

echo.
echo ============================================
echo   Installation complete!
echo   You can now run the script with:
echo   python Image_into_Sketch.py
echo ============================================

pause