log C:\Users\ichobotov\Desktop\tests\restarts\phoenix_all_gnss.log
1 print [--%t--]
s 11 12
wait 3
b 12
wait 1
$PITES,OUT.NMEA.GGA=H,1
$PITES,OUT.IPS.SV=H,1
$PITES,OUT.RT3.RAW.SET=H,1
$PITES,GNSS.SYS.IRN=ON
$PITES,GNSS.SYS.GLO=ON
$PITES,OUT.IPS.PRF=H,1
$PITES,OUT.IPS.MSEC=H,1
wait 601
u coldstart.sc