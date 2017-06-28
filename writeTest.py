test = []
test.append(10)
test.append(5)
test.append(7)
output = open("audioPVToutput.txt", "w+")
for s in test:
  output.write(str(s))
  output.write("\n")

output.close()
