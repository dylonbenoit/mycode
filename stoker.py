#!usr/bin/env python3

with open("dracula.txt","r") as foo:
    vamp_count = 0
    with open("vampytimes.txt", "w") as fang:
        for line in foo:
            if "vampire" in line.lower():
                print(line)
                vamp_count = vamp_count + 1
                fang.write(line)
    print(vamp_count)