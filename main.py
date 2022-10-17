import time

time.sleep(1)

varis = {}

var_names = []

file_path = input("File: ")

file = open(file_path, "r+")

file_read = file.read()

conts = file_read.split("\n")

for i in conts:

    if i != "" or i != " ":

        if "PRINT " in i:

            try:

                stri = i.split("PRINT")

                if '"' in stri[1]:

                    fin = stri[1].split('"')

                    print(fin[1])

                for j in var_names:

                    if j in stri[1]:

                        print(varis[j])

            except:

                try:

                    stri = i.split("PRINT")

                    fin = stri[1]

                    print(fin)

                except:

                    print("Couldn't print the number.")

        elif "WAIT" in i:

            try:

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

        elif "AUTO" in i:

            try:

                stri = i.split("AUTO")

                fin1 = stri[1].split(" ")

                var_name = fin1[1]

                var_names.append(var_name)

                if '"' in fin1[3]:

                    fin2 = fin1[3].split('"')

                    var_value = fin2[1]

                elif "TRUE" or "FALSE" in fin1[3]:

                    if "TRUE" in fin1[3]:

                        var_value = "True"

                    elif "FALSE" in fin1[3]:

                        var_value = "False"

                elif "NULL" in fin1[3]:

                    var_value = "None"

                else:

                    var_value = fin1[3]                                                                                                                                                          varis[var_name] = var_value

                print(varis)

            except:

                print("Couldn't define variable.")                                                                                                                               

        elif "QUIT" in i:

            quit()
