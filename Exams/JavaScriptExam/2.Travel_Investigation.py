data = input().strip('[').replace("\"",'').strip(', ')
delimiter = input().strip(",")
delimiter = delimiter.replace("\"", '')
some_text = input().strip(' ]')

company_list = []
companies = data.split(delimiter)
for company in companies:
	company = company.strip(' ')
	company_list.append(company)

print(company_list)
valid_s = []
invalid_s = []
while len(some_text) > 0:
	some_text = some_text.strip("\"\,\'")
	some_text_list = some_text.lower().split(' ')
	#print(company_list,some_text_list)
	#if set(company_list).issubset(set(some_text_list)):
	if all(x in some_text_list for x in company_list):
	#if set(company_list) <= set(some_text_list):
		valid_s.append(some_text)
	else:
		invalid_s.append(some_text)

	some_text = input().strip("]")

if len(valid_s) > 0:
	print('ValidSentences')
	for num,sen in enumerate(valid_s):
		numb = str(num+1) + '.'
		print(numb,valid_s[num].lower())
if len(invalid_s) > 0:
	print('InvalidSentences')
	print('==============================')
	for num,sen in enumerate(invalid_s):
		numb = str(num+1) + '.'
		print(numb,invalid_s[num].lower())



