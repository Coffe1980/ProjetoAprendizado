n =input('Olá! Qual é seu nome> ')
s = input('Qual é seu salário atual>  ')
print(n, s,'suas informações estão corretas?')
r = input('Sim ou Não> ')
if r == 'Sim' or r == 'sim' or r == 'S' or r == 's':
    print('Ok!')
else:
    print("Vai tomar no cu então")
    quit()
print('Ok!')
h = input('informe sua carga horária>  ')
print( "Seu salario é {:.} mensal, sua carga horaria é {} dado essas informações você ganha {} por hora.".format( s, h, int(s)/int(h)))