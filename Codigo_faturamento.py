def calculaMenor(file):
    menor = -1
    objMenor = {}
    for obj in file:
        valorAtual = obj['valor']
        if menor == -1 or valorAtual < menor and valorAtual != 0.0:
            menor = valorAtual
            objMenor = obj
    print("Menor valor: dia " + str(objMenor["dia"]) + ", Valor: " + str(objMenor["valor"]))

def calculaMaior(file):
    maior = -1
    objMaior = {}
    for obj in file:
        valorAtual = obj['valor']
        if maior == -1 or valorAtual > maior and valorAtual != 0.0:
            maior = valorAtual
            objMaior = obj
    print("Maior valor: dia " + str(objMaior["dia"]) + ", Valor: " + str(objMaior["valor"]))

def calculaMedia(file):
    valorTotal = 0
    diasUteis = 0
    
    for obj in file:
        valorAtual = obj['valor']
        if valorAtual > 0:
            diasUteis = diasUteis + 1
            valorTotal = valorTotal + valorAtual
    
    media = valorTotal / diasUteis
    
    qtdeDias = 0
    
    for obj in file:
        valorAtual = obj['valor']
        if valorAtual > media:
            qtdeDias = qtdeDias + 1
    print("Média: " + str(media))
    print("Dias maiores que a média: " + str(qtdeDias))
        
    
    
 
file = [
	{
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
	{
		"dia": 6,
		"valor": 26742.6612
	},
	{
		"dia": 7,
		"valor": 0.0
	},
	{
		"dia": 8,
		"valor": 42889.2258
	},
	{
		"dia": 9,
		"valor": 46251.174
	},
	{
		"dia": 10,
		"valor": 11191.4722
	},
	{
		"dia": 11,
		"valor": 0.0
	},
	{
		"dia": 12,
		"valor": 0.0
	},
	{
		"dia": 13,
		"valor": 3847.4823
	},
	{
		"dia": 14,
		"valor": 373.7838
	},
	{
		"dia": 15,
		"valor": 2659.7563
	},
	{
		"dia": 16,
		"valor": 48924.2448
	},
	{
		"dia": 17,
		"valor": 18419.2614
	},
	{
		"dia": 18,
		"valor": 0.0
	},
	{
		"dia": 19,
		"valor": 0.0
	},
	{
		"dia": 20,
		"valor": 35240.1826
	},
	{
		"dia": 21,
		"valor": 43829.1667
	},
	{
		"dia": 22,
		"valor": 18235.6852
	},
	{
		"dia": 23,
		"valor": 4355.0662
	},
	{
		"dia": 24,
		"valor": 13327.1025
	},
	{
		"dia": 25,
		"valor": 0.0
	},
	{
		"dia": 26,
		"valor": 0.0
	},
	{
		"dia": 27,
		"valor": 25681.8318
	},
	{
		"dia": 28,
		"valor": 1718.1221
	},
	{
		"dia": 29,
		"valor": 13220.495
	},
	{
		"dia": 30,
		"valor": 8414.61
	}
]

calculaMenor(file)
calculaMaior(file)
calculaMedia(file)
