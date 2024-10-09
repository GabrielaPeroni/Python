# Iniciando variaveis globais
estoque_atual = {
    "farinha": 0,  # 0g
    "acucar": 0,   # 0g
    "ovos": 0,     # 0 ovos
    "leite": 0,    # 0ml
    "manteiga": 0, # 0g
    "fermento": 0, # 0g
    "baunilha": 0  # 0ml
} # estoque inicial

bolo_preco = {
    "farinha": {"preco": 6.0, "quantidade": 1000}, # 1000g de farinha  // 6.0 reais
    "acucar": {"preco": 4.0, "quantidade": 1000} , # 1000g de açúcar   // 4.0 reais
    "ovos": {"preco": 8.0, "quantidade": 12},      # 12 ovos           // 8.0 reais
    "leite": {"preco": 5.0, "quantidade": 1000},   # 1000ml de leite   // 5.0 reais
    "manteiga": {"preco": 10.0, "quantidade": 200},# 200g de manteiga  // 10.0 reais
    "fermento": {"preco": 8.0, "quantidade": 100}, # 100g de fermento  // 8.0 reais
    "baunilha": {"preco": 10.0, "quantidade": 50}  # 50ml de baunilha  // 10.0 reais
} # quantidade e preco Mercado

bolo = { 
    "farinha": 500, # 500g de farinha
    "acucar": 300,  # 300g de açúcar
    "ovos": 4,      # 4 ovos
    "leite": 200,   # 200ml de leite
    "manteiga": 100,# 100g de manteiga
    "fermento": 10, # 10g de fermento
    "baunilha": 10  # 10ml de baunilha
}# Receita Bolo

def preco(numero_bolos, bolo_preco, bolo, estoque_atual):
    custo_final = 0  # iniciando custo zerado
    compra_final = 0
    compras = {}  # quantidade de compras feitas, e estoque novo

    for ingrediente, quantidade_requerida in bolo.items():
        # quantidade por bolo
        quantidade_total_necessaria = quantidade_requerida * numero_bolos

        # pegando ingredientes do dict
        if ingrediente in bolo_preco:  
            preco_estoque = bolo_preco[ingrediente]
            quantidade_estoque = preco_estoque["quantidade"]
            preco_unitario = preco_estoque["preco"]

            quantidade_em_estoque = estoque_atual.get(ingrediente, 0)

            # confirmar valor no estoque antes da compra
            if quantidade_total_necessaria > quantidade_em_estoque:  
                quantidade_faltante = quantidade_total_necessaria - quantidade_em_estoque

                # quantos comprar
                unidades_para_comprar = (quantidade_faltante + quantidade_estoque - 1) // quantidade_estoque
                quantidade_necessaria = unidades_para_comprar * quantidade_estoque 
                custo_ingrediente = (quantidade_necessaria / quantidade_estoque) * preco_unitario

                custo_final += custo_ingrediente
                compra_final += unidades_para_comprar

                # update de estoque
                estoque_atual[ingrediente] = quantidade_necessaria - quantidade_faltante

                compras[ingrediente] = {
                    'quantidade_comprada': quantidade_necessaria,
                    'unidades_compradas': unidades_para_comprar,
                    'custo': custo_ingrediente
                }

            else:
                # update de estoque
                estoque_atual[ingrediente] -= quantidade_total_necessaria  

    return custo_final, compra_final, compras, estoque_atual

def estoque(bolo_preco, bolo, num_bolos, estoque_atual):
    custo_gas_eletrico = (7.0 + 5.0) * num_bolos
    margem_lucro = 50/100 # %50 de lucro escolhido

    # Pegando valores da função
    custo_final, compra_final, compras, estoque_atual = preco(num_bolos, bolo_preco, bolo, estoque_atual)
    preco_fatia = (custo_final + custo_gas_eletrico) / (num_bolos * 12)

    print("\n", "="*80)
    print(f"> \033[31mCusto total para {num_bolos} bolos:\033[0m  R${custo_final + custo_gas_eletrico:.2f} \33[37m((R${custo_final:.2f}//Ingredientes + R${custo_gas_eletrico:.2f} //Gás e Eletricidade))\033[0m")
    print(f"> \033[34mLucro por bolo (margem de 50%):\033[0m  R${(custo_final + custo_gas_eletrico) * margem_lucro:.2f} (Preço de venda: R${(custo_final + custo_gas_eletrico)/num_bolos:.2f}  //Venda com lucro: R$R${(((custo_final + custo_gas_eletrico) * margem_lucro) + (custo_final + custo_gas_eletrico))/num_bolos:.2f})")
    print(f"> \033[34mLucro por fatia (margem de 50%):\033[0m  R${preco_fatia * margem_lucro:.2f} (Preço de venda: R${preco_fatia:.2f}  //Venda com lucro: R${preco_fatia + (preco_fatia * margem_lucro):.2f})")


    print("="*80)

    print("\n>> \33[33mINGREDIENTES COMPRADOS:\033[0m")
    for ingrediente, info in compras.items():
        quantidade_comprada = info['quantidade_comprada']
        unidades_compradas = info['unidades_compradas']
        custo = info['custo']

        # ingredientes comprados
        if ingrediente in ["leite", "baunilha"]:
            print(f"- {unidades_compradas} x {ingrediente} ({quantidade_comprada}ml) -> Custo: R${custo:.2f}")
        elif ingrediente == "ovos":
            print(f"- {unidades_compradas} x duzia {ingrediente} ({quantidade_comprada} ovos) -> Custo: R${custo:.2f}")
        else:
            print(f"- {unidades_compradas} x {ingrediente} ({quantidade_comprada}g) -> Custo: R${custo:.2f}")
    print(f"-"*50, f"\n>> Total : {compra_final} itens -> Custo: R$ {custo_final}")

    print("\n>> \33[33mESTOQUE ATUAL:\033[0m")
    # estoque atual
    for ingrediente, quantidade in estoque_atual.items():
        if ingrediente in ["leite", "baunilha"]:
            print(f"- {quantidade}ml de {ingrediente}")
        elif ingrediente == "ovos":
            print(f"- {quantidade} ovos")
        else:
            print(f"- {quantidade}g de {ingrediente}")

    # Ingredientes necessários para o próximo bolo
    ingredientes_a_comprar = []
    for ingrediente, quantidade_estoque in estoque_atual.items():
        quantidade_necessaria = bolo.get(ingrediente, 0)
        if quantidade_estoque < quantidade_necessaria:
            ingredientes_a_comprar.append(ingrediente)

    # Lista de ingredientes necessários
    if ingredientes_a_comprar:
        print(f"\n>> \33[31mVocê precisa comprar os seguintes ingredientes para o próximo bolo: \033[0m", end = "")
        for ingrediente in ingredientes_a_comprar:
            print(f"{ingrediente}/ ", end = "")
        print()  # Newline after the list
    else:
        print(f"\n>> \33[33mVocê tem estoque suficiente para o próximo bolo!\033[0m")

# Inicializar variáveis globais
num_bolos = int(input("Quantos bolos deseja produzir hoje? "))

estoque(bolo_preco, bolo, num_bolos, estoque_atual)