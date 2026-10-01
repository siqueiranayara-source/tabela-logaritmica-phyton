def tabela_logaritmica(base):
    print(f"--- Tabela para a base {base} ---")
    for expoente in range(1, 11):
        resultado = base ** expoente
        print(f"{base} elevado a {expoente} = {resultado}")
    print()  # Apenas para pular uma linha entre as tabelas

# Testando com as bases solicitadas
tabela_logaritmica(2)
tabela_logaritmica(3)
tabela_logaritmica(10)
