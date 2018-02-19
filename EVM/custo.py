"""
Esse arquivo serve para calcular o custo de uma sprint
"""

def calculate():
    """
    Calcula o custo da sprint.
    """

    print("------------------------------")
    print("- Calculo de custo da sprint -")
    print("------------------------------")

    planned_points = int(input("Insira o número de pontos planejados na sprint: "))
    completed_points = int(input("Insira o número de pontos completados na sprint: "))

    cost_point = float(input("Insira o custo por ponto: "))
    sprint_developer = int(input("Insira o número de desenvolvedores trabalhando na sprint: "))
    cost_point *= sprint_developer

    planned_cost = planned_points * cost_point
    real_cost = completed_points * cost_point

    print("\n")
    print("Pontos planejados: %d" % planned_points)
    print("Pontos completados: %d" % completed_points)
    print("Custo por ponto: R$ %.2f" % cost_point)
    print("Custo planejado: R$ %.2f" % planned_cost)
    print("Custo real: R$ %.2f" % real_cost)

    if real_cost > planned_cost:
        gain = real_cost - planned_cost
        print("A sprint gerou um lucro de R$ %.2f" % gain)
    elif real_cost == planned_cost:
        print("Os custos dessa sprint está de acordo com o planejado.")
    else:
        loss = planned_cost - real_cost
        print("A sprint gerou um prejuizo de R$ %.2f" % loss)


if __name__ == '__main__':
    calculate()
