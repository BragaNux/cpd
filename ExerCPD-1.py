
#- Código em C.

# Inserionsort (int data[], int n) {
#     int tmp,i,j;
#     for (j=1;j<n;j++) {
#         i = j-1;
#         while ( (i>=0) && (tmp < data[i])) {
#             data[i+1] = data[i];
#             i--;
#         }//while
        
        
#         data[i+1] = tmp;
#     }//for
    
# }//Insertionsort


#- Código em Python

def ordenar_insercao(lista):
    comprimento = len(lista)
    for k in range(1, comprimento):
        valor_atual = lista[k]
        j = k - 1
        while j >= 0 and valor_atual < lista[j]:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = valor_atual


#já ordenados
numeros_ordenados = [10, 20, 30, 40, 50]
ordenar_insercao(numeros_ordenados)
print("Valores já ordenados:", numeros_ordenados)

#ordem inversa
numeros_invertidos = [100, 90, 80, 70, 60]
ordenar_insercao(numeros_invertidos)
print("Valores na ordem inversa:", numeros_invertidos)

#duplicados
numeros_duplicados = [15, 25, 15, 35, 25]
ordenar_insercao(numeros_duplicados)
print("Valores duplicados:", numeros_duplicados)

#aleatórios
numeros_aleatorios = [42, 7, 25, 89, 14]
ordenar_insercao(numeros_aleatorios)
print("Valores aleatórios:", numeros_aleatorios)
