import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)
import time
import sys
#import realTimeGrapher
import select

def heardEnter():
    i,o,e = select.select([sys.stdin],[],[],0.0001)
    for s in i:
        if s == sys.stdin:
            input = sys.stdin.readline()
            return True
    return False

from  PeachyGrapher import PeachyGrapher

logCount = 1
graphMin = 50
graphLastMax = 0
mesageCount = 0

firstLogString = "logCount, maxPower, date and Time"

logFile = open('logFile.csv', 'a')
logFile.write(firstLogString)
print("logged: " + firstLogString)
logFile.close()

grapher4=PeachyGrapher(numlines=3)
#grapher2=PeachyGrapher(title='TITLE',xlabel='XXX',ylabel='YYY',graphsize=20,numlines=1,legend=["string legend"],padding=2)

while True:
   ##mesageCount += 1
   if heardEnter() == True:
        logString =  str(logCount) + "," + str(graphLastMax) + "," + time.strftime("%Y:%m:%d:%H:%M:%S") + "\n"
        logFile = open('logFile.csv', 'a')
        logFile.write(logString)
	logFile.close()
        print("logged: " + logString)
        graphLastMax = 0
        logCount += 1
   mesage = int(str(ser.readline().split(',')[0])) 
   
   
   if mesage > graphLastMax:
        graphLastMax = mesage

   grapher4.addPoint([mesage,graphLastMax,graphMin])
   
#        for i in range(0,testLen):
#            rando=random.randint(0,10)
#            grapher4.addPoint([rando,rando+2,rando+5,rando-2,rando-5])
#       grapher4.saveGraph("3_line_dynamic.png")


   




