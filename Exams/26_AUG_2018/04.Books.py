data = input()


class Book:
	def __init__(self,title,author,price,chapter):
		self.title = title
		self.author = author
		self.price = price
		self.chapter = chapter


all_books = []
while data != "on work":
	chapters = data.split(' -> ')[1].split(' ')
	book_atr = data.split(' -> ')[0]
	title, author, price = book_atr.split(' ')
	if title and author and price and chapters:
		book = Book(title=title,author=author,price=price,chapter=chapters)
		all_books.append(book)

	data = input()
data = input()
while data != 'end work':
	sum_price = 0
	book_names = [x.title for x in all_books]
	if data not in book_names:
		print(f"No such book here")
	for book in all_books:
		if data == book.title:
			print(f"SOLD: {book.title} with author {book.author}. Chapters in the book {len(book.chapter)}")

	data = input()
data = input()
if len(all_books) == 0:
	print(f"Bad day :(")
for book in all_books:
	sum_price += float(book.price)
if sum_price > 0:
	print(f"Money: {sum_price:.2f}")


