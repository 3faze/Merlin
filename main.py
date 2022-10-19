import time

time.sleep(1)

vars = {}
inps = {}
var_names = []
types = ['Null', 'True', 'False']

file_path = input("File: ")

file = open(file_path, "r+")
file_read = file.read()

conts = file_read.split("\n")
for i in conts:
  if i != "" or i != " " or "//" not in i:
    if "PRINT " in i:
      try:
        stri = i.split("PRINT")
        if '"' in stri[1]:
          fin = stri[1].split('"')
          print(fin[1])
        for x in types:
          if x in stri[1]:
            print(x)
        for j in var_names:
          if j in stri[1]:
            print(vars[j])
        for z in inps:
          if z in stri[1]:
            print(inps[z])

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

    elif "VAR" in i:
      try:
        stri = i.split("VAR")
        fin1 = stri[1].split(" ")
        var_name = fin1[1]
        var_names.append(var_name)
        if '"' in fin1[3] and "VAR" in i:
          fin2 = fin1[3].split('"')
          var_value = fin2[1]
        elif "Null" in i and "VAR" in i:
          var_value = fin1[3]
        else:
          if "VAR" in i:
            var_value = fin1[3]
          else:
            print("Wrong data type")
        vars[var_name] = var_value
      except:
        print("Couldn't define variable.")

    elif "INPUT" in i:
      try:
        stri_inp = i.split("INPUT")
        inp_fin1 = stri_inp[1].split("=>")
        txt_get = stri_inp[1].split('"')[1]
        a = input(txt_get)
        txt_var = inp_fin1[1].split(" ")[1]
        inps[txt_var] = a
      except:
        print("Couldn't do an input.")

    elif "QUIT" in i:
      quit()
