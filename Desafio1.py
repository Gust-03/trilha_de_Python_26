

orcamento = int(input("insira o seu orçamento de viagem"))
destino = str(input("insira o seu destino de viagem"))
dias = int(input("insira quantos dias você pretende se hospedar"))


passagem = int(input("insira o custo da pasagem"))
hospedagem = int(input("insira o custo da hospedagem"))

hospedr = (hospedagem * dias) * 6.10
viagem = (passagem*2)
precot = viagem + hospedr

print("custo total da hospedagem:", hospedr,"reais")
print("custo da viagem:", viagem, "reais" )
print("preço total da viagem:", precot, "reais")

resto = (orcamento - precot)
faltante = (precot - orcamento) 
    
if orcamento >= precot and dias !=0: 
    print("Orçamento possível, sobrará",resto ,"reais"), print("boa viagem para", destino)
elif orcamento < precot and dias !=0: 
    print("Orçamento não possível, restam", faltante, "reais"), print("não é hoje que poderá viajar para", destino)
else: 
    print("erro, dias inválidos")
    



