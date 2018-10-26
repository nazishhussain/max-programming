import os
c=1
while c<=5:
    os.system("fswebcam -F 4 --fps 20 -r 800*600 /home/pi/NAZ/"+str(c)+".jpg")
    c = c + 1
    print("pic is taken!!!!")
