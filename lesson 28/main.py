import tkinter as ded

def hyloy(wowowowowowowowowowowowowowo):
    #print("event=", wowowowowowowowowowowowowowo)
    print("+100 gold")

root = ded.Tk()
root.title("ПЯТЁРКА ГДЕ ТАВРЫ")  # Заголовок
root.geometry("250x500")  # Разрешение окна

photo = ded.PhotoImage(file="Po_farmy_chempion.png") #,height= n

lab1 = ded.Label(root, text="nagets", image=photo)
lab1.pack()

btn = ded.Button(root)   # master - привязка к окну
# btn['command'] = hyloy  # Действие при нажатии
btn.bind("<Double-Button-1>", hyloy)
btn['text'] = "lbm"
btn['font'] = ('times new roman', 12, "bold")
btn['height'] = 2
btn['width'] = 10
btn['foreground'] = 'silver'
btn['background'] = 'black'
btn.pack(anchor = "s") # разместить    #anchor = "s" привязать кнопку к югу
root.mainloop()










# def show_message():
#
#     label['text'] = ent.get()
#     ent.delete(0, 'end')
#
#
# label = ded.Label(text="Олдам ку остальным соболезную")
# label.pack()
# ent = ded.Entry(root)
# ent.pack()
# confirm = ded.Button(text="Отправить", command= show_message)
# confirm.pack()
# root.mainloop()