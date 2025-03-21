from django.db import models

class Pessoa(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome Completo")
    phone = models.CharField(max_length=16, verbose_name="Celular")
    email = models.EmailField(verbose_name="E-mail", max_length=255)
    password = models.CharField(max_length=255, verbose_name="Senha")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True  # Torna este modelo abstrato (sem tabela própria)

class PessoaFisica(Pessoa):
    rg = models.CharField(max_length=15, verbose_name="RG")
    cpf = models.CharField(max_length=11, verbose_name="CPF")
    birth_date = models.DateField(verbose_name="Data de Nascimento")
    cep = models.CharField(max_length=9, verbose_name="CEP")


class PessoaJuridica(Pessoa):
    # Campos do responsável (pessoa física)
    rg = models.CharField(max_length=15, verbose_name="RG")
    cpf = models.CharField(max_length=11, verbose_name="CPF")
    birth_date = models.DateField(verbose_name="Data de Nascimento")
    
    # Campos do empreendimento (existentes)
    business_name = models.CharField(max_length=255, verbose_name="Nome do Empreendimento")
    cnpj = models.CharField(max_length=18, verbose_name="CNPJ")
    address = models.CharField(max_length=255, verbose_name="Endereço")
    region = models.CharField(max_length=255, verbose_name="Região")
    business_phone = models.CharField(max_length=16, verbose_name="Telefone do Empreendimento")
    business_email = models.EmailField(max_length=255, verbose_name="E-mail do Empreendimento", blank=True, null=True)
    social_media = models.CharField(max_length=255, verbose_name="Redes Sociais", blank=True, null=True)