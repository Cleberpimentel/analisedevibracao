import serial
import time
import numpy as np
import matplotlib.pyplot as plt
import os
#perguntar qual o número do ensaio para facilitar depois
ensaio = 1
while(ensaio != 0):

    ensaio = int(input('Escreva o número do ensaio: '))

    arduino = serial.Serial('COM16', baudrate = 115200)

    time.sleep(2)
    inicio = time.time() #pegando o tempo global com a função time
    segundos = [] # vai armazenar o tempo de cada medição e se tornara o eixo x
    segundos_duracao = 4

    #armazena os valores medido nos sensores
    s1 = []
    s2 = []
    c = 0
    tempo_final =  time.time() + segundos_duracao

    while time.time() < tempo_final:
        tempo = (time.time() - inicio) 
        segundos.append(float(tempo))
        valor = arduino.readline().decode().strip()
        dado1, dado2 = valor.split(",")
        s1.append(float(dado1))
        s2.append(float(dado2))
        print(f"{int(tempo)} segundos de ensaio")
        c += 1

    print(f"\nquantidade de dados {c}\n")

    with open (f"ensaios/ensaio{ensaio}sensor 2.txt",'w') as arquivo:
        for c, d in zip(s2,segundos):
            arquivo.write(f"{c}\t{d}\n")

    #escreve os dados lidos no sensor 1 em um arquivo
    with open (f"ensaios/ensaio{ensaio}sensor1.txt",'w') as arquivo:
        for a, b in zip(s1,segundos):
            arquivo.write(f"{a}\t{b}\n")

    #escreve os dados lidos no sensor 1 em um arquivo
    fig1, ax = plt.subplots()
    ax.plot(segundos, s1)
    # plt.xticks(np.arange(0, 11, 0.01))
    # plt.xlim(5, 6)
    # plt.ylim(0.12,0.15)
    ax.set_title('Dados do sensor 1')
    ax.set_xlabel('Segundos')
    ax.set_ylabel('voltts')
    plt.show()

    fig2, ax = plt.subplots()
    # plt.xticks(np.arange(0, 11, 0.01))
    ax.plot(segundos, s2)
    # plt.xlim(5, 6)
    # plt.ylim(0.13,0.16)
    ax.set_title('Dados do sensor 2')
    ax.set_xlabel('Segundos')
    ax.set_ylabel('voltts')
    plt.show()
