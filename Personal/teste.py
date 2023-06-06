def quest():
  dict_1 = {}
  count = 1
  while count == 1 :
    nome = (input('Qual seu nome?'))
    countresp = 0
    pergunta1 = input('Telefonou para a vítima? S ou N?')
    if pergunta1 == 'S' :
      countresp += 1
    pergunta2 = input('Esteve no local do crime? S ou N?')
    if pergunta2 == 'S' :
      countresp += 1
    pergunta3 = input('Mora perto da vítima? S ou N?')
    if pergunta3 == 'S' :
      countresp += 1
    pergunta4 = input('Mora perto da vítima? S ou N?')
    if pergunta4 == 'S' :
      countresp += 1
    pergunta5 = input('Já trabalhou com a vítima? S ou N?')
    if pergunta5 == 'S' :
     countresp += 1
    if countresp == 2:
      classif = 'Supeito'
    elif countresp >= 3 and countresp <= 4:
      classif = 'Cumplice'
    elif countresp == 5 :
      classif = 'Assassino'
    else:
      classif = 'Inocente'
    dict_1[nome] = (countresp,classif)
    resp2 = input('Deseja adicionar mais algum perfil? S ou N.')
    if resp2 == 'S':
      count = 1
    else:
      count = 0
  return dict_1

print(quest())