from rembg import remove
from PIL import Image

# Import original image #
img = Image.open('img.jpg')

# Remove background from image #
img_without_back = remove(img)

# Save image without background #
img_without_back.save('img_without_back.png')
