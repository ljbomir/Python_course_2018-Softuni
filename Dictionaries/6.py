def input_data(stopping_string):
    lst = []
    while True:
        data = input()
        data1 = data.split()[1:]
        if data == stopping_string:
            break
        else:
            lst.append(data1)
    return lst

#print(input_data("shopping time"))

def stock_the_shop(input_lst):
    dict = {}
    for item in input_lst:
        if item[0] in dict:
            dict[item[0]] += int(item[1])
        else:
            dict[item[0]] = int(item[1])
    return dict

shopping_time = stock_the_shop(input_data("shopping time"))
#print(shopping_time)
exam_time = input_data("exam time")
#print(shopping_time)


def odrer_from_shop(input_lst, stock_dict):
    left_in_stock = {}
    for item in input_lst:
        stock_key = item[0]
        stock_value = item[1]
        if stock_key in sorted(stock_dict):
            if int(stock_dict[stock_key]) >= int(stock_value):
                left_in_stock[stock_key] = int(stock_dict[stock_key]) - int(stock_value)
                if left_in_stock[stock_key] == 0:
                     del left_in_stock[stock_key]
            del stock_dict[stock_key]
        else:
            print(f"{stock_key} doesn't exist")

    stock_dict.update(left_in_stock)   # summ both dictionaries

    for item in sorted(stock_dict):
        stock_dict[item] = int(stock_dict[item])
        print(f"{item} -> {stock_dict[item]}")


odrer_from_shop(exam_time,shopping_time)

