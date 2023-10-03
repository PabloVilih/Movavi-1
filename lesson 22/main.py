# # # # 1 import json
# # # #
# # # # f = open("data.json", "w")
# # # # text = [False, None, 3, 3.13, (1, 2, 3)]
# # # # json.dumps(text, f, ensure_ascii=False)
# # # # f.close()
# # #
# # # f = open("data.json", "r")
# # # content
# #
# #
# #
# #
# #
# #
# #                                                                                                                                                                                             #      @
# #                                                                                                                                                                                             #      |
# #                                                                                                                                                                                             #      |
# #                                                                                                                                                                                             #     0|0
# #
# #
# 1 import json
#
#
# f = open("file.txt", "r", encoding="utf-8")
# content = json.load()
# f.close()
# print(content)
# for i, elem in enumerate(content):
#     a = type(elem)
#     if a == str:
#         content[i] += "!"
#     elif a in (int, float):
#         content[i] += 1
#     elif a == bool:
#         content[i] = not content[i]
#     elif a == list:
#         content[i] = content[i] + content[i]
#     elif elem == None:
#         content.pop(i)















import requests

position = requests.get(url="http://api.open-notify.org/iss-now.json")
data = position.json()["iss_position"]
print(f"Широта:{data['latitude']})