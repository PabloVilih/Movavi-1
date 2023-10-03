# from tkinter 1 import *
# # # # #
# # # # # def printer(pipupa):
# # # # #     print(cb_val.get())    # Booleanvar -> .get()
# # # # #     #cb.deselect()    # Снять выделение
# # # # #     #cb.select()  # Поставить выделение
# # # # #
# # # # # root = Tk()
# # # # # root.geometry("250x370")
# # # # #
# # # # # cb_val = BooleanVar()    # Переменная отвечающая за хранение значения
# # # # # cb = Checkbutton(root,
# # # # #                  text="Подписка",
# # # # #                  variable=cb_val,
# # # # #                  onvalue=True,
# # # # #                  offvalue=False)
# # # # # cb.pack()
# # # # # cb.bind("<Button-3>", printer)
# # # # #
# # # # #
# # # # # root.mainloop()
# # # # root = Tk()
# # # #
# # # #
# # # # def get_rb():
# # # #     print(rb_val.get())
# # # #
# # # #
# # # #
# # # #
# # # # root.geometry("250x370")
# # # #
# # # # rb_val = IntVar()
# # # # print(rb_val.get())
# # # # Radiobutton(root, variable=rb_val, text="Один", value=505, command=get_rb).pack()
# # # # Radiobutton(root, variable=rb_val, text="Два", value=47, command=get_rb).pack()
# # # #
# # # # root.mainloop()
# # #
# # #
# # root = Tk()
# # root.geometry("250x370")
# # #
# # # def pipu():
# # #     print(lst.curselection())   # текущий выбор
# # #
# # # v = ["Пуджик", "Сфчик", "Течес"]
# # #
# # # lst = Listbox(root,
# # #               selectmode=EXTENDED)
# # # lst.pack()
# # # for elem in v:
# # #     lst.insert("end", elem)  # размещение элемента в Listbox
# # #
# # # Button(root, text="Активировать", command=pipu()).pack()
# # #
# # #
# # #
# # #
# # # root.mainloop()
# #
# # def get_scale(e):
# #     print(scal.get())
# #     print(e)
# #
# # scal = Scale(root, from_=4, to=34,
# #              orient=HORIZONTAL,# располож
# #              length=200,  # Длинна
# #              width=20,      # Ширина
# #              tickinterval=2,
# #              command=get_scale)  # Подписать с шагом
# #
# # scal.pack()
# #
# #
# #
# #
# #
# #
# # root.mainloop()
#
# root = Tk()
# root.geometry("500x300")
#
# def activatar():
#     if btn1['state'] == "disabled": #Если кнопка выключена
#         btn1['state'] = "normal"
#     else:
#         btn1['state'] = "disabled"
#
# btn1 = Button(root, text="ШлЁп")
# btn1.pack()
#
# btn2 = Button(root, text="Процесс запуска боеголовки Альфа Активирован", command=activatar)
# btn2.pack()
#
# root.mainloop()











