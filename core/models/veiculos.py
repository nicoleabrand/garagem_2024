from django.db import models

class Veiculo(models.Model):
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    modelo = models.ForeignKey('Modelo', on_delete=models.PROTECT)
    cor = models.ForeignKey('Cor', on_delete=models.PROTECT)
    acessorios = models.ForeignKey('Acessorio', on_delete=models.PROTECT)
    
    def __str__(self):
        return f"({self.id}) {self.modelo.nome} - {self.cor.nome} - {self.ano}"