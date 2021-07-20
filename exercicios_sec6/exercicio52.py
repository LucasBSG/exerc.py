def ver_tamanho_texto(texto):

    resposta = ''

    if len(texto) >= 20:
        resposta = 'Texto muito longo!'
    else:
        resposta = 'Texto curto!'

    return resposta

texto_um = 'Lucas é estudante'

len_texto_um = ver_tamanho_texto(texto_um)

print(len_texto_um)

print(ver_tamanho_texto('Lucas gosta muito de sua mãe'))