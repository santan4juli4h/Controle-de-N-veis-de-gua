from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

# Lista de níveis do reservatório
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Função que define a cor conforme o nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Simulação do sistema
for i in range(len(niveis)):
    nivel = i + 1
    cor = definir_cor(nivel)
    print(cor + f"Nível {nivel}: {niveis[i]}")

# Reset final do estilo
print(Style.RESET_ALL)
