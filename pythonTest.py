import tkinter as tk

def startScript(event):
    print("Start button clicked")
    event.widget.pack_forget()
    packRunFrame(runFrame)
    
def packRunFrame(runFrame):
    runFrame.pack()
    
def stopScript(event):
    print("Stop button clicked")
    event.widget.pack_forget()
    packStartFrame(startFrame);
    
def packStartFrame(startFrame):
    startFrame.pack()

# def hide_me(event):
#     event.widget.pack_forget()

window = tk.Tk()
startFrame = tk.Frame(window)
startFrame.pack()
runFrame = tk.Frame(window)

greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()

# btn = tk.Button(startFrame, text="Click")
# btn.bind('<Button-1>', hide_me)
# btn.pack()
buttonStop = tk.Button(runFrame, text='Stop', width=25)
buttonStop.bind('<Button-1>', stopScript)
buttonStop.pack()

buttonStart = tk.Button(startFrame, text='Start', width=25)
buttonStart.bind('<Button-1>', startScript)
buttonStart.pack()
window.mainloop()