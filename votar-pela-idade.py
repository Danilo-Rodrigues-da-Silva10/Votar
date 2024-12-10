x = 0

x = int(input('insira sua idade: '))

if  x < 16 :
    print('você não pode votar!')
    
elif x==16: 
    print('seu voto é opcional!')

elif x==17: 
    print('seu voto é opcional!')

elif x > 60: 
    print('seu voto é opcional!')

else: 
    print('seu voto é obrigatório!')
