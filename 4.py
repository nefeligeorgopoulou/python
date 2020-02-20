# Ελέγχει εάν ο αριθμός που προκύπτει από τη μετατροπή συμβολοσειράς σε χαρακτήρες ascii είναι πρώτος ή όχι.
# Δέχεται όρισμα string, επιστρέφει boolean.
# Έχει υλοποιηθεί με συνένωση των κωδικών ASCII και όχι αριθμητική πρόσθεσή τους.
# Σε σχόλια υπάρχουν οι αλλαγές που απαιτούνται για την υλοποίηση με αριθμητική πρόσθεση.
def checkprime(userstring):
    asciistring = "" # Θα πρέπει να γίνει asciinumber = 0 στην περίπτωση της αριθμητικής πρόσθεσης.
    for stringchar in list(userstring):
        asciistring = asciistring + str(ord(stringchar)) # Θα πρέπει να γίνει asciinumber = asciinumber + ord(stringchar) στην περίπτωση της αριθμητικής πρόσθεσης.
    asciinumber = int(asciistring) # Θα πρέπει να παραληφθεί στην περίπτωση της αριθμητικής πρόσθεσης.
    for divider in range(2, asciinumber//2): # Αρκεί να ελέγξω αν διαιρείται ακριβώς μέχρι και με το μισό του asciinumber.
        if (asciinumber % divider) == 0:
            return False
            break
    else:
        return True
