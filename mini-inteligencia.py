
primeironumero=int(input("Digite o primeiro numero "))
segundonumero=int(input("Digite o segundo numero "))
terceironumero=int(input("Digite o terceiro numero "))

if primeironumero == segundonumero and terceironumero == primeironumero:
    print("O menor número é ", primeironumero)
    
else:
    if primeironumero < segundonumero and primeironumero < terceironumero:
        print("O menor numero é: ", primeironumero)
        
    else:
        if segundonumero < primeironumero and segundonumero < terceironumero:
            print("O menor numero é: ", segundonumero)
            
        else:
            print("O menor numero é: ", terceironumero)