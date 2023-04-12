x = 0
y = 0



import tkinter as ded
root = ded.Tk()
root


for row in range(3):
    for column in range(3):
        btn = ded.Button(text=f"({row},{column})")
        btn.grid(row=row, column=column)