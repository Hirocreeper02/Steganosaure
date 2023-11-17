from PIL import Image



# source = Image.open("ColorDistinction/bus_go_brrr.jpg")
source = Image.open("12345.jpg")

demonstrationImage = [
    Image.new("RGB",(source.width,source.height),(0,0,0)),
    Image.new("RGB",(source.width,source.height),(0,0,0)),
    Image.new("RGB",(source.width,source.height),(0,0,0))
]

testImage = Image.new("RGB",(source.width,source.height),(0,0,0))

for x in range(source.width):
    
    for y in range(source.height):
        
        for color in range(3):
            
            if source.getpixel((x,y))[color]%2 == 1:
                
                demonstrationImage[color].putpixel((x,y),(255,255,255))
                testImage.putpixel((x,y),(255,255,255))



demonstrationImage[0].save("demonstrationImageRed.jpg")
demonstrationImage[1].save("demonstrationImageGreen.jpg")
demonstrationImage[2].save("demonstrationImageBlue.jpg")

testImage.save("testImage.jpg")