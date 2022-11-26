sleep, 1000
CoordMode, Mouse, Screen
MouseMove, 1591, 202, 20
Click


MouseMove, 1670, 360, 30
Click
MouseClickDrag, left, 1900, 310, 1900, 920, 30
MouseMove, 1670, 652
Send, {Shift Down}
Click
Send, {Shift Up}
sleep, 100
Click, Right
MouseMove, 1700, 661, 10
Click

sleep, 2000
MouseMove, 714, 643, 20
Click
MouseMove, 1208, 905, 20
Click
sleep, 5000
MouseMove, 1183, 488, 20
Click
sleep, 2000
MouseMove, 1198, 550, 20
Click

Sleep, 50000


MouseMove, 1106, 540, 20
Click, 3
Send, ^c

if WinExist("Python 3.8.3 Shell")
    WinActivate 
else
    WinActivate, *Python 3.8.3 Shell*
	
Send, ^v
Sleep, 500
Send, {Enter}
Sleep, 500

if WinExist("Onfleet — Mozilla Firefox")
	WinActivate


MouseMove, 1106, 582, 20
Click, 3
Send, ^c

if WinExist("Python 3.8.3 Shell")
    WinActivate 
else
    WinActivate, *Python 3.8.3 Shell*
	
Send, ^v
Sleep, 500
Send, {Enter}
Sleep, 500

if WinExist("Onfleet — Mozilla Firefox")
	WinActivate


MouseMove, 1106, 631, 20
Click, 3
Send, ^c

if WinExist("Python 3.8.3 Shell")
    WinActivate 
else
    WinActivate, *Python 3.8.3 Shell*
	
Send, ^v
Sleep, 500
Send, {Enter}
Sleep, 500

if WinExist("Onfleet — Mozilla Firefox")
	WinActivate
	
	
MouseMove, 1106, 671, 20
Click, 3
Send, ^c

if WinExist("Python 3.8.3 Shell")
    WinActivate 
else
    WinActivate, *Python 3.8.3 Shell*
	
Send, ^v
Sleep, 500
Send, {Enter}
Sleep, 500

if WinExist("Onfleet — Mozilla Firefox")
	WinActivate


MouseMove, 1203, 740, 20
Click, 2
Sleep, 2000

if WinExist("Python 3.8.3 Shell")
    WinActivate 
else
    WinActivate, *Python 3.8.3 Shell*
	
