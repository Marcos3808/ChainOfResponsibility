from abc import ABC, abstractmethod

# Classe que representa um chamado de suporte
class SupportRequest:
    def __init__(self, description, difficulty, instruction):
        self.description = description
        self.difficulty = difficulty
        self.instruction = instruction

# Classe abstrata para o suporte
class Support(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass

# Suporte Nivel 1: resolve problemas simples
class SupportLevel1(Support):
    def handle_request(self, request):
        if request.difficulty == 1:
            print(f"Suporte Nivel 1 resolveu o problema: {request.description}")
            print(f"Instrucoes: {request.instruction}")
        else:
            print("Problema não absoluto para Suporte Nivel 1.")

# Suporte Nivel 2: resolve problemas intermediarios
class SupportLevel2(Support):
    def handle_request(self, request):
        if request.difficulty == 2:
            print(f"Suporte Nivel 2 resolveu o problema: {request.description}")
            print(f"Instrucoes: {request.instruction}")
        else:
            print("Problema não absoluto para Suporte Nivel 2.")

# Suporte Nivel 3: resolve problemas avancados
class SupportLevel3(Support):
    def handle_request(self, request):
        if request.difficulty == 3:
            print(f"Suporte Nivel 3 resolveu o problema: {request.description}")
            print(f"Instrucoes: {request.instruction}")
        else:
            print("Problema não absoluto para Suporte Nivel 3.")

def main():
    try:
        nivel = int(input("Digite o nivel de suporte desejado (1, 2 ou 3): "))
    except ValueError:
        print("Entrada invalida. Por favor, digite um numero.")
        return

    if nivel not in (1, 2, 3):
        print("Nivel de suporte invalido.")
        return

    if nivel == 1:
        suporte = SupportLevel1()
        print("\nProblemas disponiveis:")
        print("1 - Redefinir senha")
        print("2 - Problema com login")
        print("3 - Conta bloqueada")
        print("4 - Outro problema")
        try:
            opcao = int(input("Digite o numero do problema desejado: "))
        except ValueError:
            print("Entrada invalida.")
            return

        if opcao == 1:
            description = "Redefinir senha"
            instruction = "Verifique seu email para o link de redefinicao."
        elif opcao == 2:
            description = "Problema com login"
            instruction = "Confirme suas credenciais de login."
        elif opcao == 3:
            description = "Conta bloqueada"
            instruction = "Contate o admin para desbloquear a conta."
        elif opcao == 4:
            description = input("Digite o problema: ")
            instruction = "Problema não padrao. Contate o suporte tecnico para solução."
        else:
            print("opção invalida.")
            return

    elif nivel == 2:
        suporte = SupportLevel2()
        print("\nProblemas disponiveis:")
        print("1 - Reinstalar software")
        print("2 - Atualizar sistema")
        print("3 - Corrigir bug no aplicativo")
        print("4 - Outro problema")
        try:
            opcao = int(input("Digite o numero do problema desejado: "))
        except ValueError:
            print("Entrada invalida.")
            return

        if opcao == 1:
            description = "Reinstalar software"
            instruction = "Siga o tutorial para reinstalar o software."
        elif opcao == 2:
            description = "Atualizar sistema"
            instruction = "Use o instalador oficial para atualizar o sistema."
        elif opcao == 3:
            description = "Corrigir bug no aplicativo"
            instruction = "Reinicie o aplicativo e limpe o cache."
        elif opcao == 4:
            description = input("Digite o problema: ")
            instruction = "Problema não padrao. Contate o suporte tecnico para solução."
        else:
            print("opção invalida.")
            return

    elif nivel == 3:
        suporte = SupportLevel3()
        print("\nProblemas disponiveis:")
        print("1 - Defeito no hardware")
        print("2 - Falha no servidor")
        print("3 - Problema de rede critico")
        print("4 - Outro problema")
        try:
            opção = int(input("Digite o numero do problema desejado: "))
        except ValueError:
            print("Entrada invalida.")
            return

        if opcao == 1:
            description = "Defeito no hardware"
            instruction = "Cheque cabos e conexoes; se persistir, contate a assistencia."
        elif opcao == 2:
            description = "Falha no servidor"
            instruction = "Reinicie o servidor e verifique os logs."
        elif opcao == 3:
            description = "Problema de rede critico"
            instruction = "Revise as configuracoes de rede e reinicie o roteador."
        elif opcao == 4:
            description = input("Digite o problema: ")
            instruction = "Problema não padrao. Contate o suporte tecnico para solução."
        else:
            print("opção invalida.")
            return

    request = SupportRequest(description, nivel, instruction)
    suporte.handle_request(request)

if __name__ == "__main__":
    main()
