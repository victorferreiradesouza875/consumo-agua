#entrada
tipo_de_imovel = input("Digite o tipo de imóvel (casa, comercial ou apartamento): ").lower()
consumo = float(input("Informe o consumo mensal de água em m³: ")).replace(",", ".")
if tipo_de_imovel == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")
elif tipo_de_imovel == "apartamento" and consumo < 10:
    print("Consumo econômico – excelente controle de água!")
elif (tipo_de_imovel == "apartamento" or tipo_de_imovel == "casa") and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.")
else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")