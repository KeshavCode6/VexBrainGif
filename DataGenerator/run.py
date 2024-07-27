import os

FRAMES = 12
for i in range(FRAMES):
    os.system(f"python gifToPixels.py {i} {FRAMES} > data{i}.txt")


final = ""
for i in range(FRAMES):
    with open(f"data{i}.txt", "r") as f:
        if(i!=FRAMES-1):
            final += f.read() + ","
        else:
            final += f.read()

a = f"data = [{final}]"
with open("FINAL.txt", "w") as f:
    f.write(a)