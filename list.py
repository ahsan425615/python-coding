vrt = ["black", "green", "white", "red"]
print(vrt)
print(vrt[-1])
print(vrt[1:3])
print(vrt[:3])
vrt[3] = "yellow"
print(vrt)
print(vrt[1:1])
vrt[1:1] = ["test", "test"]
print(vrt)

for vr in vrt:
    print(vr)
    print(vrt, end="-")

if "red" in vrt:
    print("red avaiable")

vrt.pop()
vrt.remove("green")
vrt.insert(1, "pink")
print(vrt)


vrt.append("grey")
print(vrt)





















