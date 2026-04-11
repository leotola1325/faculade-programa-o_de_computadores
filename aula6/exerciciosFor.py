#escrever um  programa para um vetor de 5 medias dos alunos fazer  a somatoria e imprimir a media  da sala

medias = [5.5,10,8,1,6]
somaMedia = 0
maiorMedia = max(medias)
for media  in medias:
    somaMedia += media
    print(f'media = {media} soma = {somaMedia}')
    if media > maiorMedia:
        maiorMedia = media
    
print(somaMedia)
print(f'medida da sala = {somaMedia / len(medias)} e a maior media indivual e: {maiorMedia}')