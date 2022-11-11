from PIL import Image, ImageFilter
import cv2

#Ler imagem
im = Image.open( './images/eu.jpg' )

#Convertento imagem em tons de cinza
shade_gray = im.convert('L')

#Aplicando um filtros à imagem
blur = shade_gray.filter( ImageFilter.BLUR )
blur_kernel = blur.filter( ImageFilter.Kernel((3,3), (1,1,1,1,1,1,1,1,1),1,0) )

sharpen = shade_gray.filter( ImageFilter.SHARPEN )

find_edhes = shade_gray.filter( ImageFilter.FIND_EDGES )
find_edhes_kernel_one = find_edhes.filter( ImageFilter.Kernel((3,3), (1,0,-1,2,0,-2,1,0,-1), 1, 0) )
find_edhes_kernel_two = find_edhes.filter( ImageFilter.Kernel((3,3), (1,2,1,0,0,0,-1,-2,-1),1,0) )

#Salvando a imagem filtradas
shade_gray.save( './images/shade_gray.jpg', 'JPEG' )
blur_kernel.save( './images/image_blur.jpg', 'JPEG' )
sharpen.save( './images/image_sharpen.jpg', 'JPEG' )
find_edhes_kernel_one.save('./images/image_find_edhes_1.jpg', 'JPEG')
find_edhes_kernel_two.save('./images/image_find_edhes_2.jpg', 'JPEG')

#Calculo de imagens
im_blur = cv2.imread('./images/image_blur.jpg')
im_shade_gray = cv2.imread('./images/shade_gray.jpg')

#Subtraindo e criando  imagem orignal pelo filtro de blur
unsharp = cv2.subtract(im_shade_gray, im_blur)
cv2.imwrite("./images/unsharp.jpg", unsharp)

#Juntando e criando imagem original com o unsharp
im_unsharp = cv2.imread('./images/unsharp.jpg')
sharpening = cv2.add(im_unsharp, im_shade_gray)
cv2.imwrite("./images/sharpening.jpg", sharpening)
