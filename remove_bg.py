from PIL import Image
from rembg import remove
input_path = "D:\\photos\\IMG_20230727_130243.jpg"
output_path = "sample2.png"
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
