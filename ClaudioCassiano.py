opção = 0
while opção != 5:
    print(' SEJA BEM VINDO AO NOSSO SISTEMA SOBRE O COVID.')
    print("\nDIGITE UMA OPÇÃO DE 0 a 5 PARA EXIBIR AS INFORMAÇÕES:\n")
    print("[ 0 ] - Mostrar a porcentagem em Gênero Feminino e Masculino.")
    print("[ 1 ] - Porcentagem por Genero Feminino e Masculino.\n      - Porcentagem de jovens, adultos e idosos.\n      - Porcentagem de Quem tomou vacina e placebo.\n      - Porcentagem de Quem contraiu covid e não contraiu covid.")
    print("[ 2 ] - Porcentagem da Eficácia geral da vacina.")
    print("[ 3 ] - Porcentagem da Eficácia por jovens, adultos e idosos.")
    print("[ 4 ] - Porcentagem da Eficácia por gênero masculino e feminino.")
    print("[ 5 ] - Sair do Programa\n")

    opção = int(input("DIGITE DE 0 a 5 PARA EXIBIR AS OPÇÕES: "))
    if opção == 0:
        # Opção 0 Participantes % gênero Masculino e feminino
        arq = open('dados.txt', "r")
        linhas = arq.readlines()
        qtd = int(linhas[0])
        masc = fem = 0
        for i in range(1, qtd + 1, 1):
            p = linhas[i].replace('\n', ' ')
            if p[0] == 'M':
                masc = masc + 1
            if p[0] == 'F':
                fem = fem + 1
        masc = int(masc / qtd * 100)
        fem = int(fem / qtd * 100)
        print(f'Participantes Feminino: {fem} % e Masculino: {masc} %')
    elif opção == 1:
        arq = open('dados.txt', "r")
        linhas = arq.readlines()

        qtd = int(linhas[0])
        masc1 = fem1 = 0

        for i in range(1, qtd + 1, 1):
            p = linhas[i].replace('\n', ' ')

            if p[0] == 'M':
                masc1 = masc1 + 1
            if p[0] == 'F':
                fem1 = fem1 + 1

        masc1 = int(masc1 / qtd * 100)
        fem1 = int(fem1 / qtd * 100)

        print(f'Participantes Feminino: {fem1} %  e Masculino: {masc1} %')

        # Opção 1 linha 2 - % de jovens, adultos e idoso
        arq = open('dados.txt', 'r')
        linhas = arq.readlines()
        qtd = int(linhas[0])
        contf = 0

        lista = []
        for i in range(1, qtd + 1, 1):
            p = linhas[i].split(',')
            lista.append(int(p[1]))

        jov = adu = ido = 0
        for i in lista:
            if i <= 19:
                jov = jov + 1
            elif i > 20 and i < 59:
                adu = adu + 1
            else:
                ido = ido + 1

        jov = jov * 100 / qtd
        adu = adu * 100 / qtd
        ido = ido * 100 / qtd

        print(
            f'Participantes Jovens: {int(jov)} %, Adultos: {int(adu)} % e Idosos: {int(ido)} %')

        # Opção 1 linha 3 - Quem tomou vacina e quem tomou placebo
        arq = open('dados.txt', "r")
        linhas = arq.readlines()

        qtd = int(linhas[0])

        vac = pla = 0
        for i in range(1, qtd + 1, 1):
            p = linhas[i].split(',')
            if p[2] == 'V':
                vac = vac + 1
            if p[2] == 'P':
                pla = pla + 1
        vac = vac * 100 / qtd
        pla = pla * 100 / qtd
        print(f'Tomaram Vacina: {int(vac)} % e Placebo: {int(pla)} %')

        # Opção 1 linha 4 - Quem contraiu covid e quem não contraiu covid
        simCov = naoCov = 0
        for i in range(1, qtd + 1, 1):
            p = linhas[i].split(',')
            if p[3] == 'S\n':
                simCov = simCov + 1
            if p[3] == 'N\n':
                naoCov = naoCov + 1
        simCov = simCov * 100 / qtd
        naoCov = naoCov * 100 / qtd
        print(
            f'Contrairam covid: {int(simCov)} % e Não contrairam covid: {int(naoCov)} %')

    elif opção == 2:
        # opção 2- Eficiencia geral - placebo e pegou covide e vacina e pegou covid
        arq = open('dados.txt', "r")
        linhas = arq.readlines()
        qtd = int(linhas[0])

        a = b = 0
        for i in range(1, qtd + 1, 1):
            p = linhas[i].split(',')
            if p[2] == 'P' and p[3] == 'S\n':
                a = a + 1
            elif p[2] == 'V' and p[3] == 'S\n':
                b = b + 1

        eficacia = 100 * (a - b) / a
#print(f'Placebo que pegou covid: {ps} % \nVacina que pegou covid: {vs} %')
        print(f'Eficácia geral da vacina: {round(eficacia, 2)} %')
    elif opção == 3:

        arq = open('dados.txt', 'r')
        linhas = arq.readlines()
        qtd = int(linhas[0])

        JoP = JoV = AdP = AdV = IdP = IdV = 0
        for i in range(1, qtd + 1, 1):
            p = linhas[i].split(',')
            if int(p[1]) <= 19 and p[2] == 'P' and p[3] == 'S\n':
                JoP = JoP + 1
            if int(p[1]) <= 19 and p[2] == 'V' and p[3] == 'S\n':
                JoV = JoV + 1
            if int(p[1]) > 19 and int(p[1]) <= 59 and p[2] == 'P' and p[3] == 'S\n':
                AdP = AdP + 1
            if int(p[1]) > 19 and int(p[1]) <= 59 and p[2] == 'V' and p[3] == 'S\n':
                AdV = AdV + 1
            if int(p[1]) > 59 and p[2] == 'P' and p[3] == 'S\n':
                IdP = IdP + 1
            if int(p[1]) > 59 and p[2] == 'V' and p[3] == 'S\n':
                IdV = IdV + 1

        eficaciaJovem = 100 * (JoP - JoV) / JoP
        eficaciaAdulto = 100 * (AdP - AdV) / AdP
        eficaciaIdoso = 100 * (IdP - IdV) / IdP

        print('A eficácia para jovens é: ', int(eficaciaJovem), '%')
        print('A eficácia para adultos é: ', int(eficaciaAdulto), '%')
        print('A eficácia para os idosos é: ', int(eficaciaIdoso), '%')
    elif opção == 4:
        arq = open('dados.txt', "r")
        linhas = arq.readlines()
        qtd = int(linhas[0])

        am = bm = af = bf = 0

        for i in range(1, qtd + 1, 1):
            p = linhas[i].split(',')
            if p[0] == 'M' and p[2] == 'P' and p[3] == 'S\n':
                am = am + 1
            if p[0] == 'M' and p[2] == 'V' and p[3] == 'S\n':
                bm = bm + 1
            if p[0] == 'F' and p[2] == 'P' and p[3] == 'S\n':
                af = af + 1
            if p[0] == 'F' and p[2] == 'V' and p[3] == 'S\n':
                bf = bf + 1

        eficaciaM = 100*(am - bm)/am
        eficaciaF = 100*(af - bf)/af
        print(f'Eficácia Masculina: {int(eficaciaM)} %')
        print(f'Eficácia Feminina: {int(eficaciaF)} %')

    elif opção == 5:
        print("Você encerrou o programa.\n")


print("Fim do programa!\n")
