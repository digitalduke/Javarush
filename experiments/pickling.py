import pickle

testlist = ["Хуй", "Пизда", "Джигурда"]

with open("pickling.bin", "wb") as f:
    pickle.dump(testlist, f)

del testlist

with open("pickling.bin", "rb") as f:
    new_list = pickle.load(f)

print(new_list)
