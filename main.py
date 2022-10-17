try:

 51                 stri = i.split("AUTO")

 52                 fin1 = stri[1].split(" ")                  53                 var_name = fin1[1]                         54                 var_names.append(var_name)

 55                 if '"' in fin1[3]:

 56                     fin2 = fin1[3].split('"')

 57                     var_value = fin2[1]                    58                 elif "TRUE" or "FALSE" in fin1[3]:

 59                     if "TRUE" in fin1[3]:

 60                         var_value = "True"

 61                     elif "FALSE" in fin1[3]:

 62                         var_value = "False"

 63                 elif "NULL" in fin1[3]:

 64                     var_value = "None"                     65                 else:

 66                     var_value = fin1[3]                    67                 varis[var_name] = var_value

 68                 print(varis)

 69             except:

 70                 print("Couldn't define variable.")
