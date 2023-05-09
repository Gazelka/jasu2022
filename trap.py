import tkinter as tk
window=tk.Tk()
window.title("Lecker")
img=tk.PhotoImage(file='sweep.png')
img=img.subsample(32)
i0=tk.PhotoImage()
l=tk.Label(window,bg="light blue", image = img)
l.pack(fill=tk.BOTH, expand =True)
armed = tk.IntVar()
armed.set(0)
def klick():
    armed.set(0)
b=tk.Button(window,text="Klick mich!",bg='pink',command=klick)
b.pack(fill=tk.X)
ausweg= "bittebitte"
def handler(e):
    if e.char=='q' and armed.get()!=2:
        window.destroy()
    if e.char==ausweg[pos]:
        pos+=1
    if pos==len(ausweg):
        window.destroy()
window.bind('<Key>',handler)
def go_in(e):
    if e.widget==window:
        armed.set(1)
def go_out(e):
    if e.widget==window and armed.get()==1:
        armed.set(2)
        l.config(bg="black")
        l.config(image=i0)
        b.destroy()
        window.config(cursor='pirate')
        window.attributes("-fullscreen",True)
window.bind('<Enter>',go_in)
window.bind('<Leave>',go_out)
window.mainloop()

