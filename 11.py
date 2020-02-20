# Ελέγχει εάν υπάρχει αποθηκευμένη τετράδα αριθμών που να ικανοποιεί τη διάταξη αριθμών εισόδου.
# Δέχεται ως όρισμα εξάδα αριθμών (χωρισμένοι με κενά στο ίδιο string).
# Ενημερώνει το χρήστη για την ύπαρξη ή όχι τετράδας στο αρχείο 11.txt των τετράδων (μία τετράδα ανά γραμμή, oι αριθμοί της κάθε τετράδας χωρισμένοι με κενά).
import sys
if len(sys.argv) < 2: #Εάν ο χρήστης δεν έδωσε 6άδα αριθμών εκτελώντας το πρόγραμμα, τη ζητάω.
    usernumbers = input("Παρακαλώ εισάγετε 6 αριθμούς, χωρισμένους με κενά: ")
else:
    usernumbers = sys.argv[1]
userlist = usernumbers.split()
for eachnumber in userlist:
    try:
        float(eachnumber)
    except ValueError:
        sys.exit("Έχετε εισάγει εσφαλμένους αριθμούς!")
if len(userlist)!=6:
    sys.exit("Δεν έχετε εισάγει 6 αριθμούς!")
myfile = open("11.txt")
filenumbers = myfile.read()
myfile.close()
quadlist = [quad.split() for quad in filenumbers.split("\n")]
for candlist in quadlist:
    if candlist==userlist[0:4] or candlist==userlist[1:5] or candlist==userlist[2:]:
        print("Υπάρχει τουλάχιστον μία τετράδα αριθμών που ταιριάζει με αυτούς τους αριθμούς, η {}!".format(candlist))
        break
else:
    print("Δεν υπάρχει τετράδα αριθμών που να ταιριάζει με αυτούς τους αριθμούς!")
