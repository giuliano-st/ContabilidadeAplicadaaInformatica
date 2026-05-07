import pandas as pd

def ler_planilha(caminho):
    df = pd.read_excel(caminho, names=['nome', 'tipo', 'valor'], skiprows=2)

    return df.to_dict(orient='records')

def classificar_conta(contas):
    balanco = { #Dicionário das contas
        "ativo" : [],
        "passivo" : []
    }
    palavras_passivo = ["financiamento", "empréstimo", "contas a pagar", "fornecedores", "salários"]
    palavras_ativo = ["caixa", "banco", "aplicações", "clientes", "estoque",
                "cartões", "móveis", "máquinas", "veículos", "softwares", "imóveis"]
    for conta in contas:
      nome = str(conta["nome"]).lower()

      if any(p in nome for p in palavras_passivo):
          conta["tipo"] = "passivo"
          balanco['passivo'].append(conta)

      elif any(p in nome for p in palavras_ativo):
          conta["tipo"] = "ativo"
          balanco['ativo'].append(conta)

      else:
          conta["tipo"] = "passivo"
          balanco['passivo'].append(conta)

    return balanco

def somar_balanco(balanco_total):
    total_ativos = sum(item["valor"] for item in balanco_total['ativo'])
    total_passivos = sum(item["valor"] for item in balanco_total['passivo'])

    patrimonio_liquido = total_ativos - total_passivos
    print(f"Balanço: ")
    print(f"Total Ativo:  R$ {total_ativos:,.2f}")
    print(f"Total Passivo: R$ {total_passivos:,.2f}")
    print(f"Patrimônio Líquido: R$ {(total_ativos - total_passivos):,.2f}")


def main():
  caminho = "Contas.xlsx"
  lista_bruta = ler_planilha(caminho)
  balanco_final = classificar_conta(lista_bruta)
  print(f"Contas:")
  for item in lista_bruta:
    print(f"{item["nome"], item["tipo"], item["valor"]}")
  somar_balanco(balanco_final)
if __name__ == "__main__":
  main()