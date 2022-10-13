import time

file = open("file.mer", "r+")                                         file_read = file.read()
conts = file_read.split("\n")                                         
for i in conts:
    if i != "" or i != " ":
        if "PRINT " in i:                                                         #print("Token found:", "PRINT")
            try:
                stri = i.split("PRINT")
                fin = stri[1].split('"')[1]
                print(fin)
            except:
                try:
                    stri = i.split("PRINT")
                    fin = stri[1]
                    print(fin)
                except:
                    print("Couldn't print the number.")
        elif "WAIT" in i:                                                         try:
                stri = i.split("WAIT")
                fin = stri[1]
                time.sleep(float(fin))
            except:
                print("Couldn't delay the program.")

        elif "EVAL" in i:
            try:
                stri = i.split("EVAL")
                fin1 = stri[1].split("(")
                fin2 = fin1[1].split(")")
                print(eval(fin2[0]))
            except:
                print("Couldn't execute the expression")
