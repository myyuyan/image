from PIL import Image

numbers = []

for i in range(1,41):
    if i%2!=0:
        numbers.append(i)

for num in numbers:
    img1 = Image.open('./number/%d.png'%num)
    img2 = Image.open('./number/%d.png'%(num+1))
    size1, size2 = img1.size, img2.size
    print(size1)
    joint = Image.new('RGB', (5000, int(5000/210*297)),(255,255,255))
    loc1, loc2 = (int(2500-size1[0]/2), int((5000/210*297/2-size1[1])/2)), (int(2500-size1[0]/2), int((5000/210*297/2-size1[1])/2+5000/210*297/2))
    joint.paste(img1, loc1)
    joint.paste(img2, loc2)
    joint.save('./view/%d.png'%num)