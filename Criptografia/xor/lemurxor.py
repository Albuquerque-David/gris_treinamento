from PIL import Image, ImageChops

#Armazena as imagens na variavel.

lemur = Image.open("lemur.png")
flag = Image.open("flag.png")

#Adiciona as imagens.

result = ImageChops.add(lemur, flag)
result.save("result_add.png")

#Subtrai as imagens.

result = ImageChops.subtract(lemur, flag)
result.save("result_subtract.png")

#XOR nas imagens.

lemur = lemur.convert('1')
flag = flag.convert('1')

result = ImageChops.logical_xor(lemur,flag)
result.save("result_xor.png")