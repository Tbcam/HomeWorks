def sansur(cumlelistesi,yasaklıkelime,yenikelime):
    cumlelistesi = cumlelistesi.split(" ")
    sonuc = " "
    for i in range(len(cumlelistesi)):
        if cumlelistesi[i] == yasaklıkelime:
            cumlelistesi[i] = yenikelime
    return (sonuc.join(cumlelistesi))



