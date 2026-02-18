# 19-m
davlatlar = {"UZ": "O'zbekiston",
             "RU": "Rossiya",
             "US": "Amerika",
             "TR": "Turkiya"
}

print(davlatlar)

for davlatlar in davlatlar:
    print(davlatlar)



# 20-m
baholar = {"Matematika": 5,
           "Fizika": 4,
           "Kimyo": 5,
           "Biologiya": 4,
           "Tarix": 5
}

print(baholar)

for i in baholar:
    print(i)

print(baholar.items())



# 21-m
shaxs = {"ism": "Jamshid",
         "yosh": 21,
         "shahar": "Xorazm",
         "kasb": "Talaba"
}

print(shaxs)



# 22-m
dict1 = {"a": 1,
         "b": 2}
dict2 = {"c": 3,
         "d": 4}
dict3 = {"e": 5,
         "f": 6
}

print(dict1, dict2, dict3)

birlashtirilgan = {**dict1, **dict2, **dict3}

print(birlashtirilgan)


# 23-m
talaba = {
    "ism": "Nodira",
    "familiya": "Rahimova",
    "yosh": 20,
    "kurs": 3,
    "fakultet": "Dasturiy injiniring",
    "stipendiya": True
}

print(talaba)


# 24-m
narxlar = {
    "Non": 3000,
    "Sut": 9000,
    "Tuxum": 18000,
    "Go'sht": 85000,
    "Yog'": 45000,
    "Sabzi": 7000
}

print(narxlar)

print(narxlar["Go'sht"])


# 25-m
matn = "salom dunyo salom python python python dunyo"

print(matn)

print(f"Salomlar soni : {matn.count('salom')}")
print(f"Dunyolar soni : {matn.count('dunyo')}")
print(f"Pythonlar soni : {matn.count('python')}")


