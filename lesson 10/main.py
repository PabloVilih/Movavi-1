# # # while True:
# # #     try:
# # #         x = int(input("Ярусов: "))
# # #         if x < 1:
# # #             raise Exception("f")
# # #     except ValueError:
# # #         print("за такие шутки в американских школах убивают")
# # #         continue
# # #     except Exception as error_message:
# # #         print("ОШИБКА", error_message)
# # #         continue
# # #     else: #если ошибок нет
# # #         break # выход из while true
# # #
# # # while True:
# # #     char = input("Символ: ").strip()
# # #     if len(char) != 1:
# # #         print("Хочу 1 пицу")
# # #     else:
# # #         break
# # #
# # #
# # # for asd in range(1, x + 1):
# # #     # левая половина
# # #     print(" " * (x - asd), end="")
# # #     print(char * asd, end="||")
# # #
# # #     # правая половина
# # #     print(char * asd)
# # x = int(input("Число: "))
# # for yltro_mega_seper_Anton in range(1, 11):
# #     print(x, "x", yltro_mega_seper_Anton, "=", x * yltro_mega_seper_Anton)
#
# xzb = int(input("Ширина: "))
# xzh = int(input("Высота:"))
#
# for _ in range(0, xzh):
#     print("# " * xzb)