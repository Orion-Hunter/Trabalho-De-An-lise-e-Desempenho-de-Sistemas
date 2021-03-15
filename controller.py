def tempo_de_espera_fila(taxa_media_de_chegada, taxa_media_de_atendimento):
       return round((taxa_media_de_atendimento / (taxa_media_de_chegada*(taxa_media_de_chegada-taxa_media_de_atendimento))) * 60, 5)
   

def tempo_de_espera_sistema(taxa_media_de_chegada, taxa_media_de_atendimento):
       return round((1 / (taxa_media_de_chegada-taxa_media_de_atendimento)) * 60, 5)
   
