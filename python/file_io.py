lyrics = """\
No life till leather
We are gonna kick some ass tonight
We got the metal madness
When our fans start screaming
It's right well alright
When we start to rock
We never want to stop again
"""

with open("lyrics.txt", "w") as f:
    f.write(lyrics)

with open("lyrics.txt", "r") as f:
    for line in f:
        print(line, end="")
