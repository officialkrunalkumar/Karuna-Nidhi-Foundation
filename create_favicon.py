from PIL import Image

img = Image.open('Foundation_Logo.png').convert('RGBA')
img = img.resize((64, 64), Image.LANCZOS)
img.save('favicon.png')
print('favicon.png created')
