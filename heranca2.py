from heranca import Animal, Gato, Cachorro
mico = Gato("Mico", "gato", 4)
print(f"Meu gato é o {mico.nome}")
mico.patas = 2
mico.respirar()
mico.ronronar()
mico.rugir()
print("----------------------------------------")
trovao = Cachorro("Trovão", "pincher", 2)
trovao.abanar_rabo()
trovao.respirar()
trovao.rugir()