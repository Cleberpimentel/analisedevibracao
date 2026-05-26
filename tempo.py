import time

segundos_duracao = 10
inicio = time.time()
tempo_final =  time.time()+ segundos_duracao
print(tempo_final)
tempos = []
while time.time() < tempo_final:
    tempo = (time.time() - inicio) + 1
    tempos.append(tempo)
    print(f"{int(tempo)} Processando dados...")

print(tempos)
print("O tempo acabou! Loop encerrado")
# nome = []
# a = input('letra')
# while a.isalpha():
#     a = input('letra')
#     if a.isalpha():
#         nome.append(a)
#     else:
#         print(nome)
