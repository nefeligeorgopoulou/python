# Τριπλασιάζει έναν αριθμό, προσθέτει 1 και αθροίζει τα ψηφία του τελικού αριθμου.
# Δέχεται όρισμα string, επιστρέφει string.
def domagic(stringnumber):
    numericnumber = float(stringnumber)
    numericnumber = numericnumber * 3 + 1
    listnumber = list(str(numericnumber))
    digitsum = 0
    for digit in listnumber:
        if digit.isnumeric(): digitsum = digitsum + int(digit)
    print("Μετά τις πράξεις, ο αριθμός έχει γίνει {}.".format(digitsum))
    return str(digitsum)

# Ζητά από το χρήστη εισαγωγή αριθμού και τον ενημερώνει για το πως έγινε αυτός, μετά τις πράξεις της domagic().
# Ο αριθμός εισόδου μπορεί να είναι είτε ακέραιος, είτε δεκαδικός (θετικός ή αρνητικός).
while True:
    userinput = input("Έναν αριθμό, παρακαλώ: ")
    try:
        float(userinput)
        break
    except ValueError:
        print("Πάμε πάλι!", end=" ")
        continue
while True:
    userinput = domagic(userinput)
    if len(userinput)==1:
        break
