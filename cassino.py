import random
import time
import sys
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_animacao():
    simbolos = ["🍒", "🍋", "🍇", "🔔", "⭐", "💎"]
    for _ in range(5):
        print(f"| {random.choice(simbolos)} | {random.choice(simbolos)} | {random.choice(simbolos)} |", end="\r")
        time.sleep(0.2)
    print(" " * 20, end="\r")

def girar_rolo():
    simbolos = ["🍒", "🍋", "🍇", "🔔", "⭐", "💎"]
    return random.choice(simbolos)

def jogar():
    print("\nCaça-Níquel Python")
    mostrar_animacao()
    
    resultado = [girar_rolo(), girar_rolo(), girar_rolo()]
    print(f"| {resultado[0]} | {resultado[1]} | {resultado[2]} |")
    
    if resultado[0] == resultado[1] == resultado[2]:
        print("WIN!")
    elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
        print("QUASEE")
    else:
        print("Não soltou cartinha")

if __name__ == "__main__":
    while True:
        jogar()
        print("\nEnter = para jogar novamente  / q = sair")
        resposta = sys.stdin.readline().strip().lower()
        if resposta == 'q':
            print("Obrigado")
            break
        limpar_terminal()
