
with open ('34data_sent_rmspace.txt', 'w') as output:
	with open('34data_sent.txt', 'r') as f:
		for line in f:
			if line != '\n':
				output.write(line)