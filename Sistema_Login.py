import time
"Sistema de cadastro em Python com login e senha (exercicio de aprendizado)"
"O sistema contara com um sistema de cadastramento e apos o cadastro sera"
"verificado se os dados estão corretos seguindo a logica do programa"

print('-----Bem-vindo(a)-----')
time.sleep(2)
print('Informe as seguintes informações')
cadastro = input('Informe seu usuario: ')
senha = input("Crie uma senha: ")

print("Armazenando os dados...")
time.sleep(2)
print("Dados armazenados com sucesso!")

print("Tela de login")
login = input("Informe seu usuario: ")
loginsenha = input("Informe sua senha: ")

if cadastro == login and senha == loginsenha:
    print("Sistema acessado com sucesso")
else:
    print("Usuario ou senha incorreto")





