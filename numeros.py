print(f'{'.is_integer()':-^32}')
# Verifica se o valor do float é um inteiro (ou seja, não tem parte fracionária). Retorna 
#True se o valor for um inteiro, False caso contrário.
n_1 = 23.00
n_2 = 23.10
print('n_1 ->',n_1.is_integer())
print('n_2 ->',n_2.is_integer())

print(f'\n{'.to_bytes':-^32}')
# Retorna uma representação em bytes do inteiro.
n_3 = 1024
print('n_3 ->', n_3.to_bytes(2, 'big'))
n_4 = 10
print('n_4 ->', n_4.to_bytes(2, 'big'))
n_5 = 10
print('n_5 ->', n_5.to_bytes())


