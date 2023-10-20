
import segno as sg

from urllib.request import urlopen

song_url = sg.make_qr("https://www.youtube.com/watch?v=60do5EDAM3M")
gif_url = urlopen("https://media.tenor.com/M0Sy7NiaaX4AAAAC/red-heart-heart.gif")
# qr_code = sg.make_qr("Hello, World!")
# qr_code_rotate = qr_code.to_pil(scale=5,border=10,dark="green",light="darkorange",quiet_zone="yellow",data_dark="teal").rotate(45)


song_url.to_artistic(
    background = gif_url,
    target = "animated_qr_code.gif",
    scale=5,border=10,dark="green",light="darkorange",quiet_zone="yellow",data_dark="teal"
    )
# qr_code_rotate.save("advanced_qrcode.png")



