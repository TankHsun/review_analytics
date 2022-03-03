data = []
count = 0
sum_all = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		sum_all += len(line)
		if count % 10000 == 0:
			print('讀取進度', len(data)/10000,'%')
print('留言平均長度為', sum_all/len(data))


	