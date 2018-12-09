# dit={"name":"wmd","age":26,"sex":"nv"}
# # print(dit)
# dit["name"]="gx"
# print(dit)
# dit["birth"]="0526"
# print(dit)
# del dit["name"]
# print(dit)
# for key1 in dit:
#     print(dit[key1])
# for value in dit.values():
#     print(value)
# for value in dit.items():
#     print(value)
#
#
# print(len(dit))

# 练习1

list=[{"name":"wmd","sex":"nv","age":21,"birth":526,"email":"12345@qq.com"},
      {"name":"qmd","sex":"nan","age":25,"birth":626,"email":"212345@qq.com"},
      {"name": "emd","sex": "nan", "age": 27, "birth": 726, "email": "312345@qq.com"}]
listnan=[]
listnv=[]
# for i in list:
#         if i["sex"]=="nan":
#             listnan.append(i)
#         else:
#             listnv.append(i)
# print(listnan)
# print(listnv)

for i in list:
    # print(i)
    if i["sex"]=="nan":
        listnan.append(i)
print(i)


