
f_out = open("./Final_Frequency_List_For_Task.txt", "w+")

with open("./misc_files/Hindi_Frequency_List_Full_Wiki.txt") as f:
	lines = f.read().split('\n')
	#print(lines)

	already_done_words = []
	count_old = 0
	count_new = -1
	

	with open("./misc_files/hin.freq.categorised.txt") as f2:

		lines2 = f2.read().split('\n')
		#print(lines2)

		for line2 in lines2:
			word2 = line2.split('/')

			if len(word2) > 1 and '$' in word2[1]:
				already_done_words.append(word2[1].split('*')[1].split('$')[0].strip())

		for line in lines:
			freq = line.split('\t')[1]
			word = line.split('\t')[2].split(' ')[0].strip()

			if word in already_done_words:
				count_old += 1
			else:
				count_new += 1
				print(str(count_new) + "\t" + freq + "\t" + word + "\n")
		

		print("Old words:", count_old)
		print("New words:", count_new)