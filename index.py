# =========================================================
# RPG BOKU NO HERO - HISTÓRIA COMPLETA
# =========================================================
# RPG inspirado em Boku no Hero Academia
# Agora com:
# ✔ História
# ✔ Escolhas variáveis
# ✔ Sistema de XP
# ✔ Níveis
# ✔ Bosses
# ✔ Missões
# ✔ Final diferente dependendo das escolhas
# =========================================================

import random
import time
import sys

# 👇 função de barra de vida

def barra_vida(atual, maximo):

    barras = int((atual / maximo) * 10)

    barra = "█" * barras + "░" * (10 - barras)

    return f"{barra} {atual}/{maximo} HP"


#  slow, função para de dialogos

def slow(txt, vel=0.03):

    for letra in txt:
        print(letra, end="", flush=True)
        time.sleep(vel)

    print()

# =========================================================
# FUNÇÃO DE TEXTO DEVAGAR
# =========================================================

def escrever(texto):

    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.02)

    print()

# =========================================================
# HERÓI
# =========================================================

heroi = {
    "nome": "",
    "quirk": "",
    "vida": 100,
    "vida_max": 100,
    "dano": 0,
    "xp": 0,
    "nivel": 1,
    "dinheiro": 0
}

# =========================================================
# ESCOLHA DO PERSONAGEM
# =========================================================

escrever("====================================")
escrever("      RPG BOKU NO HERO")
escrever("====================================\n")

escrever("Escolha seu personagem:")
escrever("1 - Deku")
escrever("2 - Bakugou")
escrever("3 - Todoroki")
escrever("4 - Dabi")
escrever("5 - Tsukuyomi")
escrever("6 - Criar personagem")

escolha = input("\nDigite: ")

# =========================================================
# PERSONAGENS
# =========================================================

if escolha == "1":

    heroi["nome"] = "Deku"
    heroi["quirk"] = "One For All"
    heroi["dano"] = 21

elif escolha == "2":

    heroi["nome"] = "Bakugou"
    heroi["quirk"] = "Explosão"
    heroi["dano"] = 20

elif escolha == "3":

    heroi["nome"] = "Todoroki"
    heroi["quirk"] = "Gelo e Fogo"
    heroi["dano"] = 25
elif escolha == "4":

    heroi["nome"] = "Dabi"
    heroi["quirk"] = "cremation"
    heroi["dano"] = 33

elif escolha == "5":

    heroi["nome"] = "Tsukuyomi"
    heroi["quirk"] = "Dark Shadow"
    heroi["dano"] = 29

elif escolha == "6":

    heroi["nome"] = input("Nome do herói: ")

    heroi["quirk"] = input("Nome da individualidade: ")

    while True:

        dano = int(input("Dano inicial (5-33): "))

        if 5 <= dano <= 30:
            break

        print("Escolha um valor entre 5 e 33.")

    heroi["dano"] = dano
else:
    escrever("Escolha inválida.")
    exit()

# =========================================================
# INTRODUÇÃO
# =========================================================

escrever("\n====================================")
escrever("               HISTÓRIA")
escrever("====================================\n")

escrever(
f"{heroi['nome']} sempre sonhou em ser "
"o maior herói do Japão."
)

escrever(
"Após entrar para a U.A., "
"uma ameaça misteriosa apareceu na cidade."
)

escrever(
"Vilões começaram a atacar pessoas "
"em Musutafu."
)

escrever(
"All Might desapareceu misteriosamente..."
)

escrever(
"E agora cabe a você salvar a cidade."
)

input("\nPressione ENTER para continuar...")

# =========================================================
# STATUS
# =========================================================

def status():

    escrever("\n====================================")
    escrever(f"HERÓI: {heroi['nome']}")
    escrever(f"INDIVIDUALIDADE: {heroi['quirk']}")
    escrever(f"VIDA: {heroi['vida']}")
    escrever(f"NÍVEL: {heroi['nivel']}")
    escrever(f"XP: {heroi['xp']}")
    escrever(f"DINHEIRO: {heroi['dinheiro']}")
    escrever("====================================")

# =========================================================
# GANHAR XP
# =========================================================

def ganhar_xp(valor):

    heroi["xp"] += valor

    escrever(f"\nVocê ganhou {valor} XP!")

    while heroi["xp"] >= 100:

        heroi["xp"] -= 100
        heroi["nivel"] += 1
        heroi["vida"] = heroi["vida_max"]
        heroi["dano"] += 5

        escrever("\n====================================")
        escrever("VOCÊ SUBIU DE NÍVEL!")
        escrever(f"NÍVEL ATUAL: {heroi['nivel']}")
        escrever("Seu dano aumentou!")
        escrever("Sua vida foi restaurada!")
        escrever("====================================")

# =========================================================
# SISTEMA DE BATALHA
# =========================================================

def batalha(nome, vida, vida_max, dano):

    escrever("\n====================================")
    escrever(f"BATALHA CONTRA {nome.upper()}!")
    escrever("====================================")

    while vida > 0 and heroi["vida"] > 0:

        escrever(barra_vida(heroi["vida"], 100))
        escrever(barra_vida(vida, vida_max))
        escrever("\n1 - Ataque Fraco")
        escrever("2 - Ataque Forte")
        escrever("3 - Curar")

        escolha = input("\nEscolha: ")

        # =================================================
        # ATAQUE FRACO
        # =================================================

        if escolha == "1":

            ataque = random.randint(5, 10) + heroi["dano"]

            vida -= ataque

            escrever(
            f"\nVocê atacou e causou {ataque} de dano!"
            )

        # =================================================
        # ATAQUE FORTE
        # =================================================

        elif escolha == "2":

            chance = random.randint(1, 100)

            if chance <= 55:

                ataque = random.randint(15, 25) + heroi["dano"]

                vida -= ataque

                escrever(
                f"\nCRÍTICO! Você causou {ataque}!"
                )

            else:

                escrever("\nVocê errou!")

        # =================================================
        # CURA
        # =================================================

        elif escolha == "3":

            cura = random.randint(15, 30)

            heroi["vida"] += cura

            if heroi["vida"] > 100:
                heroi["vida"] = 100

            escrever(
            f"\nVocê recuperou {cura} de vida!"
            )

        else:

            escrever("\nEscolha inválida!")
            continue

        # =================================================
        # ATAQUE INIMIGO
        # =================================================

        if vida > 0:

            ataque_inimigo = random.randint(5, dano)

            heroi["vida"] -= ataque_inimigo

            escrever(
            f"{nome} causou {ataque_inimigo} de dano!"
            )

    # =====================================================
    # RESULTADO
    # =====================================================

    if heroi["vida"] <= 0:

        escrever("\n====================================")
        escrever("VOCÊ FOI DERROTADO...")
        escrever("====================================")
        exit()

    else:

        escrever(f"\nVocê derrotou {nome}!")

# =========================================================
# MISSÃO 1
# =========================================================

escrever("\n====================================")
escrever("MISSÃO 1 - SALVAR CIVIS")
escrever("====================================")

escrever(
"Um grupo de vilões atacou uma estação."
)

escrever(
"Você vê duas opções:"
)

escrever("\n1 - Salvar os civis")
escrever("2 - Perseguir o vilão principal")

missao1 = input("\nEscolha: ")

# =========================================================
# ESCOLHAS
# =========================================================

if missao1 == "1":

    escrever(
    "\nVocê salvou dezenas de pessoas!"
    )

    # diálogo feito pela função slow
   
    slow(f"civis: Obrigado por nos salvar, {heroi['nome']}!")
    slow("civis:Você apareceu quando todos estavam com medo...")
    slow("civis:Agora sabemos que ainda existem verdadeiros heróis!")
    slow(f"{heroi['nome']}: Fico feliz por vocês estarem bem.")
    slow(f"{heroi['nome']}: Enquanto eu estiver aqui, ninguém vai machucar vocês.")
    slow(f"{heroi['nome']}: Um herói sempre protege quem precisa!")

    heroi["dinheiro"] += 100

    ganhar_xp(50)

else:

    escrever(
    "\nVocê perseguiu o vilão."
    )

    escrever(
    "Mas vários civis ficaram feridos..."
    )

    ganhar_xp(20)

# =========================================================
# PRIMEIRA BATALHA
# =========================================================

batalha("Vilão de Lama", 60, 60, 15)

ganhar_xp(50)

# =========================================================
# MISSÃO 2
# =========================================================

escrever("\n====================================")
escrever("MISSÃO 2 - ATAQUE À U.A.")
escrever("====================================")

escrever(
"Os vilões invadiram a escola U.A."
)

escrever(
"Você encontra uraraka presa."
)

escrever("\n1 - Ajudar uraraka")
escrever("2 - Ir direto lutar")

missao2 = input("\nEscolha: ")

if missao2 == "1":

    slow(f"uraraka: muito obrigado {heroi['nome']}, estou te devendo um favor!")
    
    escrever(
    "\nUraraka ficou te devendo um favor."
    )

    heroi["dano"] += 5
    ajuda_uraraka = True

else:

    escrever(
    "\nVocê ignorou Uraraka."
    )

    ajuda_uraraka = False


# =========================================================
# SEGUNDA BATALHA
# =========================================================

slow("\nUm Nomu apareceu!")

vida_nomu = 120

# Uraraka ajuda antes da luta
if ajuda_uraraka:

    slow("\nUraraka entrou na batalha para te ajudar!")

    dano_uraraka = 20

    vida_nomu -= dano_uraraka

    slow(f"Uraraka causou {dano_uraraka} de dano!")

    slow(barra_vida(vida_nomu, 120))

# batalha principal
batalha("Nomu", vida_nomu, 120, 25)

ganhar_xp(100)

# =========================================================
# TERCEIRA MISSÃO
# =========================================================

escrever("\n====================================")
escrever("MISSÃO EXTRA - ATAQUE NOTURNO")
escrever("====================================")

escrever(
"Durante a noite, um vilão destrói lojas no centro da cidade."
)

escrever(
f"{heroi['nome']} corre para impedir o ataque."
)

escrever(
"Os civis estão fugindo desesperados..."
)

slow("civil: Por favor herói, pare ele!")
slow(f"{heroi['nome']}: Eu não vou deixar ninguém se ferir!")

# =========================================================
# NOVA BATALHA
# =========================================================

batalha("Stain", 90, 90, 20)

# =========================================================
# RECOMPENSAS
# =========================================================

escrever(
"\nStain foi derrotado e os civis foram salvos!"
)

heroi["dinheiro"] += 150

ganhar_xp(70)

escrever(
f"\n você recebeu 150 moedas!"
)

# =========================================================
# FINAL
# =========================================================

escrever("\n====================================")
escrever("FINAL")
escrever("====================================")

if heroi["nivel"] >= 3:

    escrever(
    f"\n{heroi['nome']} se tornou "
    "um dos maiores heróis da U.A!"
    )

else:

    escrever(
    f"\n{heroi['nome']} ainda tem "
    "muito a aprender..."
    )

escrever("\nFIM DO JOGO.")