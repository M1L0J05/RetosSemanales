# * Crea un programa que calcule quien gana más partidas al piedra,
# * papel, tijera, lagarto, spock.
# * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# * - La función recibe un listado que contiene pares, representando cada jugada.
# * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
# *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
# * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
# * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

### Reglas:
# "🗿" --> "🦎"-"✂️"
# "📄" --> "🖖"-"🗿"
# "✂️" --> "🦎"-"📄"
# "🦎" -->  "🖖"-"📄"
# "🖖" --> "✂️"-"🗿"

import random

who_wins = {
    '🗿': ['🦎', '✂️'],
    '📄': ['🗿', '🖖'],
    '✂️': ['📄', '🦎'],
    '🦎': ['🖖', '📄'],
    '🖖': ['🗿', '✂️'],
}

moves = {
    '1':'🗿',
    '2':'📄',
    '3':'✂️',
    '4':'🦎',
    '5':'🖖'
}


def main():
    print('Bienvenido al juego "Piedra, Papel, Tijeras, Lagarto, Spock".\n')
    print('Menu de movimientos:\n1- 🗿 Piedra\n2- 📄 Papel\n3- ✂️  Tijeras\n4- 🦎 Lagarto\n5- 🖖 Spock\n')
    
    player = 0
    cpu = 0
    cont = 0

    while cont < 5:
        player_move = input('Player 1 - Inserta el número de tu movimiento. ')
        cpu_move = str(random.randint(1,5))

        if player_move != cpu_move:
            if moves[cpu_move] in who_wins[moves[player_move]]:
                player += 1
            else:
                cpu += 1
        
        print(f'{moves[player_move]} vs {moves[cpu_move]}')
        cont +=1

    
    if player != cpu:
        if player > cpu:
            print('The Winer is Player')
        else:
            print('The Winer is CPU')
    else:
        print('Tie!!')

main()
