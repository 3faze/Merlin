import time
import sys

time.sleep(1)

# -----------------------------------------------------
conts_e = None

def exec(conts_e):
  if conts_e != "" or conts_e != " " or "//" not in conts_e:
    if "PRINT " in conts_e:
      try:
        stri = conts_e.split("PRINT")
        if '"' in stri[1]:
          fin = stri[1].split('"')
          print(fin[1])
        for x in types:
          if x in stri[1]:
            print(x)
        for j in var_names:
          if j in stri[1]:
            print(varis[j])
        for z in inps:
          if z in stri[1]:
            print(inps[z])
      except:
        try:
          stri = conts_e.split("PRINT")
          fin = stri[1]
          print(fin)
        except:
          print("Couldn't print the number.")
    elif "WAIT" in conts_e:
      try:
        stri = conts_e.split("WAIT")
        fin = stri[1]
        time.sleep(float(fin))
      except:
        print("Couldn't delay the program.")
    elif "EVAL" in conts_e:
      try:
        stri = conts_e.split("EVAL")
        fin1 = stri[1].split("(")
        fin2 = fin1[1].split(")")
        print(eval(fin2[0]))
      except:
        print("Couldn't execute the expression")
    elif "VAR" in conts_e:
      try:
        stri = conts_e.split("VAR")
        fin1 = stri[1].split(" ")
        var_name = fin1[1]
        var_names.append(var_name)
        if '"' in fin1[3] and "VAR" in conts_e:
          fin2 = fin1[3].split('"')
          var_value = fin2[1]
        elif "Null" in conts_e and "VAR" in conts_e:
          var_value = fin1[3]
        else:
          if "VAR" in conts_e:
            var_value = fin1[3]
          else:
            print("Wrong data type")
        varis[var_name] = var_value
      except:
        print("Couldn't define variable.")
    elif "INPUT" in conts_e:
      try:
        stri_inp = conts_e.split("INPUT")
        inp_fin1 = stri_inp[1].split("=>")
        txt_get = stri_inp[1].split('"')[1]
        a = input(txt_get)
        txt_var = inp_fin1[1].split(" ")[1]
        inps[txt_var] = a
      except:
        print("Couldn't do an input.")
    elif "QUIT" in conts_e:
      quit()

# -----------------------------------------------------

varis = {}
inps = {}
var_names = []
types = ['Null', 'True', 'False']

file_path = sys.argv[1]

file = open(file_path, "r+")
file_read = file.read()

conts = file_read.split("\n")
for i in conts:
  if i != "" or i != " " or "//" not in i:
    if "PRINT " in i and not "FOR" in i:
      try:
        stri = i.split("PRINT")
        fin1 = stri[1].split(" ")
        fin = stri[1].split('"')
        if '"' in stri[1]:
          print(fin[1])
        elif fin1[1] in var_names or fin1[1] in inps or fin1[1] in types:
          for x in types:
            if x in fin1[1]:
              print(x)
          for j in var_names:
            if j in fin1[1]:
              print(varis[j])
          for z in inps:
            if z in fin1[1]:
              print(inps[z])

      except:
        try:
          stri = i.split("PRINT")
          fin = stri[1]
          print(fin)
        except:
          print("Couldn't print the number.")
    elif "WAIT" in i and not "FOR" in i:
      try:
        stri = i.split("WAIT")
        fin = stri[1]
        time.sleep(float(fin))
      except:
        print("Couldn't delay the program.")

    elif "EVAL" in i and not "FOR" in i:
      try:
        stri = i.split("EVAL")
        fin1 = stri[1].split("(")
        fin2 = fin1[1].split(")")
        print(eval(fin2[0]))
      except:
        print("Couldn't execute the expression")

    elif "VAR" in i and not "FOR" in i:
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
        varis[var_name] = var_value
      except:
        print("Couldn't define variable.")

    elif "INPUT" in i and not "FOR" in i:
      try:
        stri_inp = i.split("INPUT")
        inp_fin1 = stri_inp[1].split("=>")
        txt_get = stri_inp[1].split('"')[1]
        a = input(txt_get)
        txt_var = inp_fin1[1].split(" ")[1]
        inps[txt_var] = a
      except:
        print("Couldn't do an input.")

    elif "FOR" in i:
      stri = i.split("FOR")
      fin1 = stri[1].split(" ")
      brack1 = stri[1].split("(")
      brack2 = brack1[1].split(")")
      #Brack2[0] is the index to the execution
      for f_loop in range(int(fin1[3])):
        exec(brack2[0])
    elif "IF" in i and "FOR" not in i:
        stri = i.split("IF")
        fin1 = stri[1].split(" ")
        name = fin1[1]
        value = fin1[3]
        cond1 = stri[1].split("(")
        cond2 = cond1[1].split(")")
        if '"' in value:
            vfin1 = value.split('"')
            value = vfin1[1]
        else:
            pass

        if value in varis[name]:
            exec(cond2[0])
        else:
            pass

    elif "QUIT" in i:
      quit()
