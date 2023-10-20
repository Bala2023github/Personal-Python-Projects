import segno as sg

from urllib.request import urlopen

song_url = sg.make_qr("https://www.youtube.com/watch?v=9coA7bcpJII")
gif_url = urlopen("https://im.ezgif.com/tmp/ezgif-1-0c10d03806.gif")
# qr_code = sg.make_qr("./imgs/dosthi.gif")
# qr_code_rotate = qr_code.to_pil(scale=5,border=10,dark="green",light="darkorange",quiet_zone="yellow",data_dark="teal").rotate(45)


song_url.to_artistic(
    background = gif_url,
    target = "animated_qr_code_2.gif",
    scale=20,border=10,dark="green",light="darkorange",quiet_zone="yellow",data_dark="teal"
    )
# qr_code_rotate.save("advanced_qrcode.png")



