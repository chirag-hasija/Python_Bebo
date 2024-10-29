dict = {"Chirag":22,"Ajay":23,"Daksh":23}
k = "Chirag"
for x in dict.keys():
    if(k == x):
        print(dict[k])
        break
    else:
        print("Key not found")