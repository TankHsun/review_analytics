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

#單字記數
wc={} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
while True:
	search = input('你要查詢的單字為(o u t:離開)')
	if search =='o u t':
		break
	else:
		if search in wc:
			print(wc[search])
		else:
			print('查無此單字')
