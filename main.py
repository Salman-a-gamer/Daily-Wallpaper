from datetime import date
from PIL import Image, ImageDraw, ImageFont
import ctypes
import os

# --------------------
# CALCULATE DAYS LEFT
# --------------------
today = date.today()
end = date(today.year, 12, 31)
days_left = (end - today).days

# --------------------
# CREATE WALLPAPER
# --------------------
WIDTH, HEIGHT = 1920, 1080
img = Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(img)

text = f"{days_left}"

font = ImageFont.truetype(
    "C:/Windows/Fonts/georgia.ttf", 200
)

bbox = draw.textbbox((0, 0), text, font=font)
x = (WIDTH - (bbox[2] - bbox[0])) // 2 - bbox[0]
y = (HEIGHT - (bbox[3] - bbox[1])) // 2 - bbox[1]

draw.text((x, y), text, fill=(255, 255, 255), font=font)

# SAVE AS BMP (IMPORTANT)
wallpaper_path = os.path.abspath("wallpaper.bmp")
img.save(wallpaper_path, "BMP")

# --------------------
# SET WALLPAPER (WINDOWS)
# --------------------
SPI_SETDESKWALLPAPER = 20
SPIF_UPDATEINIFILE = 1
SPIF_SENDCHANGE = 2

ctypes.windll.user32.SystemParametersInfoW(
    SPI_SETDESKWALLPAPER,
    0,
    wallpaper_path,
    SPIF_UPDATEINIFILE | SPIF_SENDCHANGE
)

print("Wallpaper updated successfully!")
