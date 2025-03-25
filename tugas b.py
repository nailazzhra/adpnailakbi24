while True:
    password = input("hayoo apa passwordnya?: ")

    upper = False
    lower = False
    number = False
    character = False
    char = "!@#$%^&*()_+{}:\"<>?[]"
    capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"

    if len(password) < 8:
        print("pendek amat, minimal 8 karakter ya bub \n")
        continue
  
    for huruf in password:
        if huruf in capital:
            upper = True
        elif huruf in lowercase:
            lower = True
        elif huruf in numbers:
            number = True
        elif huruf in char:
            character = True
        
    if upper == False:
        print("jangan huruf kecil semua kek! kasi minimal 1 kapital \n")
        continue
    if lower == False:
        print("jangan capslock dong! kasi huruf kecil 1 kek \n")
        continue
    if number == False:
        print("kasi angka bro, lu ga pusing liat huruf semua? \n")
        continue
    if character == False:
        print("yang aneh-aneh lah biar ga mudah dibobol, kasi karakter khusus ya bub \n")
        continue
    
    print("NAH BENER PASSWORDNYA!")
    break