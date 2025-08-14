import random
import time
import sys

def mostrar_animacao():
    simbolos = ["🍒", "🍋", "🍇", "🔔", "⭐", "💎"]
    for _ in range(5):
        print(f"| {random.choice(simbolos)} | {random.choice(simbolos)} | {random.choice(simbolos)} |", end="\r")
        time.sleep(0.2)
    print(" " * 20, end="\r")  # limpa a linha

def girar_rolo():
    simbolos = ["🍒", "🍋", "🍇", "🔔", "⭐", "💎"]
    return random.choice(simbolos)

def jogar():
    print("\n=== 🎰 Caça-Níquel Python 🎰 ===")
    mostrar_animacao()
    
    resultado = [girar_rolo(), girar_rolo(), girar_rolo()]
    print(f"| {resultado[0]} | {resultado[1]} | {resultado[2]} |")
    
    if resultado[0] == resultado[1] == resultado[2]:
        print("\n💎 JACKPOT! Você ganhou! 💎")
    elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
        print("\n✨ Quase lá! Duas combinações iguais. ✨")
    else:
        print("\n❌ Não foi dessa vez. Tente de novo!")

if __name__ == "__main__":
    while True:
        jogar()
        print("\nPressione ENTER para jogar novamente ou digite 'q' para sair.")
        resposta = sys.stdin.readline().strip().lower()
        if resposta == 'q':
            print("\n🎯 Obrigado por jogar! Até a próxima!")
            break