# 4. ANALIZA SLJEDEĆIH WHILE PETLJI

# Što će se ispisati tijekom izvođenja sljedeće petlje:
broj = 0

while broj < 5:
    broj += 2
    print(broj) # 2 4 6
    
# Objasnite zašto je prikazana petlja beskonačna
broj = 0

while broj < 5:
    broj += 1
    print(broj)
    broj -= 1
    
#### jer se broj nikad ne povećava nego se vrijednost stalno smanjuje zbog broj -= 1

# Što ne valja u sljedećoj petlji
broj = 10

while broj > 0:
    broj -= 1
    print(broj)
    if broj < 5:
        broj += 2
        
### opet imamo beskonačnu petlju jer imamo ovaj uvjet while broj > 0: a nikad neće biti ispunjen jer se broj stalno povećava broj += 2
        