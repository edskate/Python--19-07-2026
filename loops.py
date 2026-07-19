
# contador = 1

# while contador <= 10:
 # print(f"Contagem atual: {contador}")
 # contador = contador + 1
 
 
senha = "calabreso123"
tentativa_senha = ""

while tentativa_senha != senha:
    tentativa_senha = input("Digite sua senha: ")

    if tentativa_senha != senha:
        print("👉 Senha incorreta, tente novamente.")
    else:
        print("👉 Acertou!")