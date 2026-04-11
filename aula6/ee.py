import math
medias = [5.5,10,8,1,6]
somaMedia = 0
maiorMedia = max(medias)
for media  in medias:
    somaMedia += media
    print(f'media = {media} soma = {somaMedia}')
    
print(somaMedia)
print(f'medida da sala = {somaMedia/5} e a maior media indivual e: {maiorMedia}')