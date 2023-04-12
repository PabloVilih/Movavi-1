import tkinter as ded

root = ded.Tk()
root.title("/")
root.geometry("400x400")
lab1 = ded.Label(root, text="Ваш адрес:")
lab1.pack()
ent = ded.Entry(root)
ent.pack()
lab2 = ded.Label(root, text="Коментарий:")
lab2.pack()
txt = ded.Text(root, width= 20, height= 10)
txt.pack()
btn = ded.Button(root)
btn['text'] = "Отправить"
btn['font'] = ('times new roman', 12, "bold")
btn['height'] = 2
btn['width'] = 10
btn['foreground'] = 'white'
btn['background'] = 'black'
btn.pack()





root.mainloop()