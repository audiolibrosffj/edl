

edl = open("becquer.edl", encoding="utf8")
data = edl.read()

data = data.replace("  AX       V     C        ", "")
data = data.replace("  AX       A     C        ", "AUDIO///")
data = data.replace("  BL       V     C        ", "")

print (data)

data = data.split("AUDIO")

print (data)

chapters = []

for x in data:
    x = x[x.find("///"):x.find(".wav")]
    print(x)

    
    frame = x[27:38]

    time =frame[:-3]

    h = frame[:2]
    m = frame[3:5]
    s = frame[6:8]
    f = frame[9:]

    if len(h) > 0:
        h = int(h)
        m = int(m)
        s = int(s)
        f = int(f)

        frame = f + (s*30) + (m*60*30) + (h*60*60*30)

        print(frame)

    framef = x[39:51]

    print(framef)

    hf = framef[:2]
    mf = framef[3:5]
    sf = framef[6:8]
    ff = framef[9:]
    
    if len(hf) > 0:
        hf = int(hf)
        mf = int(mf)
        sf = int(sf)
        ff = int(ff)

        framef = ff + (sf*30) + (mf*60*30) + (hf*60*60*30)

    


    name = x[x.find("NAME: ")+6:]

######    full = time + " - " + name + " " + str(frame) + " " + str(framef)
    
    full = name + " " + str(frame) + " " + str(framef)
    
    chapters.append(full)


c = str(chapters)

c = c.replace("[' - ', '", ""). replace("']", "").replace("', '", "\n")

output = open("capitulos.txt", "w+")

output.write(c)
output.close()

