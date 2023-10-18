def numPacientes():
    quantPacientes = int(input("Digite a quantidade de pacientes: "))
    infoPacientes = []

    for i in range(quantPacientes):
        print(f"Informe os dados do paciente {i + 1}: ")
        nome = input("Nome do paciente: ")
        altura = float(input("Altura em metros: "))
        peso = float(input("Peso em kg: "))

        imc = calcIMC(altura, peso)  # Chama a função calcIMC para calcular o IMC

        infoPacientes.append({
            "Nome": nome,
            "Altura (m)": altura,
            "Peso (kg)": peso,
            "IMC": imc
        })

    return infoPacientes  # Retorna a lista de informações dos pacientes

def calcIMC(altura, peso):
    imc = peso / (altura ** 2)
    return imc  # Retorna o valor do IMC calculado

def resultado(infoPacientes):
    print("\nResultado do IMC: ")

    for paciente in infoPacientes:
        print(f"Nome: {paciente['Nome']}")
        print(f"Altura: {paciente['Altura (m)']} metros")
        print(f"Peso: {paciente['Peso (kg)']} kg")
        print(f"IMC: {paciente['IMC']:.2f}")
        print("-" * 30)

infoPacientes = numPacientes()  # Chama a função numPacientes para coletar os dados
resultado(infoPacientes)  # Chama a função resultado para exibir os resultados