for i in range(5):
    meme_dict = {
                "CRINGE": "Algo vergonhoso ou constrangedor",
                "STALKEAR": "Investigar a vida de alguém online",
                "CRINGE": "algo vergonhoso ou constrangedor",
                "VDD": "abreviação da palavra 'verdade'",
                "BISCOITAR": " postar algo apenas para chamar a atenção",
                "HATER": "pessoa que está constantemente criticando os outros",
                "VLW": "abreviação da palavra 'valeu'"
    } 
    word = input("Bem vindo amigo(a), Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): " )

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Desculpe essa palavra não existe no nosso banco de dados")
