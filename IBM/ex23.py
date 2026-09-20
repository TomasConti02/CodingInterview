def checkPalindromeFormation(a, b):

    def pal(s, left, right):
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    
    def check_cross(str1, str2):
        left=0
        right=len(str2)-1
        while left<right and str1[left] == str2[right]:
            left+=1
            right-=1
        return pal(str1, left, right) or pal(str2, left, right)

    return check_cross(a, b) or check_cross(b, a)


# Caso 1: Funziona con prefisso di 'a' e suffisso di 'b'
# a: "ula" + "cfd"
# b: "jiz" + "alu"
# Risultato: ula + alu = ulaalu (Vero)
print("Caso 1 (ulaalu):", checkPalindromeFormation("ulacfd", "jizalu")) 

# Caso 2: Funziona grazie al centro di 'a' che è un palindromo
# a: "ab" + "cdc" + "xy"
# b: "qw" + "ert" + "ba"
# Risultato: ab + cdc + ba = abcdcba (Vero)
print("Caso 2 (abcdcba):", checkPalindromeFormation("abcdcyx", "qwertba"))

# Caso 3: Nessuna combinazione è possibile
# Le estremità non combaciano o i centri non sono palindromi. (Falso)
print("Caso 3 (Falso):", checkPalindromeFormation("abcde", "fghij"))

# Caso 4: Una delle due stringhe è già un palindromo di base
# Basta tagliare all'inizio (o alla fine) a prescindere dall'altra parola. (Vero)
print("Caso 4 (Già palindromo):", checkPalindromeFormation("ababa", "xyzuv"))