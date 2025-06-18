start cmd /k python radar.py
:loop
timeout /t 10 >nul
python data.py
goto loop
 
