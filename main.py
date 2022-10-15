def exec(file_path):
    import time
    time.sleep(1)

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
            
            elif "QUIT" in i:
                quit()


path = input("File: ")
print("**** COMMODORE 64 BASIC V2 ****")
print("64K RAM SYSTEM   38911 BASIC BYTES FREE")
saved = None
run = True
while run:
    main = input("> ")
    if main == "RUN":
        exec(path)
        print("READY.")
    elif main == "LIST":
        print("----------------")
        with open(path, "r+") as file:
            for j in file.readlines():
                print(j, end="")
            print("\n----------------")
    elif main == "CLEAR":
        file = open(path, "r+")
        file.truncate(0)
    elif main == "QUIT":
        quit()
    else:
        with open(path, "r+") as file:
            save = file.readlines()
            if "\n" not in file:
                file.write("\n" + main)
            else:
                file.write(main + "\n")