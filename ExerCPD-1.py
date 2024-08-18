
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

def insertion_sort(data):
    n = len(data)
    for j in range(1, n):
        tmp = data[j]
        i = j - 1
        while i >= 0 and tmp < data[i]:
            data[i + 1] = data[i]
            i = i - 1
        data[i + 1] = tmp

data = int(input("Informe os valores pra lista"))
insertion_sort(data)
print(data)
