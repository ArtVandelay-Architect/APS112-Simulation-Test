CoordMode, Mouse, Screen

if WinExist("Onfleet — Mozilla Firefox")
	WinActivate
else
	MouseMove, 1591, 202, 20
	Click

send ^{f5}
Sleep, 7000
MouseMove, 1888, 192, 20
Click
Sleep, 1000

if WinExist("Python 3.8.3 Shell")
    WinActivate 
else
    WinActivate, *Python 3.8.3 Shell*
