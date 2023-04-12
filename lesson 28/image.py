import tkinter as ded

root = ded.Tk()
img = ded.PhotoImage(file="psfp5.png")
label = ded.Label(image=img)

img2 = img.zoom(5, 1)
label2 = ded.Label(image=img2)
label2.pack()

img3 = img.subsample(2, 2)
label3 = ded.Label(image=img3)
label3.pack()

root.mainloop()
