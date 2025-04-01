aliquota1 = 0.23
aliquota2 = 0.35
aliquota3 = 0.43
scaglione1 = 28000
scaglione2 = 50000
imposta = 0
reddito =int(input("inserisci il reddito: "))

if reddito<= scaglione1:
  imposta = reddito * aliquota1
else:
    if reddito > scaglione1 and reddito <= scaglione2:
        imposta = reddito ( scaglione1 * aliquota1 + (reddito -scaglione1) * aliquota2)
    else:
        imposta = ( scaglione1 * aliquota1 + (scaglione2-scaglione1) * aliquota2 + (reddito - scaglione2) * aliquota3)
print("limposta da pagare è:", imposta)
