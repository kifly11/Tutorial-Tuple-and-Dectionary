dictA= {"nama1":"jane doe","nama2":"jhon smith","nama3":"bob stone","telp1":"+27 555 5379","telp2":"+27 555 6254","telp3":"+27 555 5689"}
print "Data Nomer Telphone"
print "________________________________"
print "|    Name    | Telphone Number |"
print "________________________________"
print "|",dictA["nama1"]," |",dictA["telp1"]," |","\n","|",dictA["nama2"]," |",dictA["telp2"]," |","\n","|",dictA["nama3"]," |",dictA["telp3"]," |"
print "________________________________"

dictA["telp1"]="+27 55 1024"
print "\nUbah Nomer Telp Jane"
print "________________________________"
print "|   Name  |  Telphone Number   |"
print "________________________________"
print "|",dictA["nama1"]," |",dictA["telp1"]," |","\n","|",dictA["nama2"]," |",dictA["telp2"]," |","\n","|",dictA["nama3"]," |",dictA["telp3"]," |"
print "________________________________"

dictA["nama4"]="Anna Copper"
dictA["telp4"]="+27 555 3237"
print "\n Menambah Data Baru"
print "________________________________"
print "|   Name   |  Telphone Number  |"
print "________________________________"
print "|",dictA["nama1"]," |",dictA["telp1"]," |","\n","|",dictA["nama2"]," |",dictA["telp2"]," |","\n","|",dictA["nama3"]," |",dictA["telp3"]," |","\n","|",dictA["nama4"]," |",dictA["telp4"]," |"
print "________________________________"
print "\n Cetak Nomer Telphone Bob Stone : ",dictA["telp3"]

print "\n Cetak Semua Key: ",dictA.keys()
print "\n Cetak Semua Value: ",dictA.values()                                                                                                                                                                                      
                                                                                                                                                                                       
