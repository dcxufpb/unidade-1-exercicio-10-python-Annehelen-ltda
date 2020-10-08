# coding: utf-8
def isEmpty(value:str) -> bool:
        return (value == None) or (len(value) == value.count(" "))


class Loja:
  
  def __init__(self, nome_loja, logradouro, numero, complemento, bairro, 
               municipio, estado, cep, telefone, observacao, cnpj,
               inscricao_estadual):
    self.nome_loja = nome_loja
    self.logradouro = logradouro
    self.numero = numero
    self.complemento = complemento
    self.bairro = bairro
    self.municipio = municipio
    self.estado = estado
    self.cep = cep
    self.telefone = telefone
    self.observacao = observacao
    self.cnpj = cnpj
    self.inscricao_estadual = inscricao_estadual

  def dados_loja(self):
    # Implemente aqui
    if (isEmpty(self.nome_loja)):
      raise Exception("O campo nome da loja é obrigatório")
    if (isEmpty(self.logradouro)):
      raise Exception("O campo logradouro do endereço é obrigatório")

    numero = int()
    try:
      numero = int(self.numero)
    except Exception:
      numero = 0
    if(numero<=0):
      numero = "s/n"

    if(isEmpty(self.cnpj)):
        raise Exception("O campo CNPJ da loja é obrigatório")
    if (isEmpty(self.municipio)):
        raise Exception("O campo município do endereço é obrigatório")
    if (isEmpty(self.estado)):
        raise Exception("O campo estado do endereço é obrigatório")
    if (isEmpty(self.inscricao_estadual)):
        raise Exception("O campo inscrição estadual da loja é obrigatório")

    part2 = f"{self.logradouro}, {numero}"
    if not isEmpty (self.complemento):
      part2 += f" {self.complemento}"
    part3 = str()
    if not isEmpty (self.bairro):
        part3 += f"{self.bairro} - "
    part3 += f"{self.municipio} - {self.estado}"
    part4 = str()
    if not isEmpty (self.cep):
        part4 = f"CEP:{self.cep}"
    if not isEmpty(self.telefone):
        if not isEmpty(part4):
            part4 += " "
        part4 += f"Tel {self.telefone}"     
    if not isEmpty(part4):
        part4 += "\n"
    part5 = str()
    if not isEmpty(self.observacao):
        part5 += f"{self.observacao}"
    
    output = f"{self.nome_loja}\n"
    output += f"{part2}\n"
    output += f"{part3}\n"
    output += f"{part4}"
    output += f"{part5}\n"
    output += f"CNPJ: {self.cnpj}\n"
    output += f"IE: {self.inscricao_estadual}"
    return output
