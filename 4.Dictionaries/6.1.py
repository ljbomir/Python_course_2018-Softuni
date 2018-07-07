def input_data(stopping_string):
    lst = []
    while True:
        data = input()
        if data == stopping_string:
            break
        else:
            lst.append(data.split()[1:])
    return lst


# print(input_data("shopping time"))

def stock_the_shop(input_lst):
    products = {}
    for product in input_lst:
        if product[0] in products:
            products[product[0]] += int(product[1])
        else:
            products[product[0]] = int(product[1])
    return products


shopping_time = stock_the_shop(input_data("shopping time"))
# print(shopping_time)
exam_time = input_data("exam time")
# print(shopping_time)


def order_from_shop(input_lst, stock_dict):
    for item in input_lst:
        stock_key = item[0]
        stock_value = item[1]
        if stock_key in stock_dict:
            if stock_dict[stock_key] > 0:
                stock_dict[stock_key] -= int(stock_value)
            else:
                print(f"{stock_key} out of stock")

        else:
            print(f"{stock_key} doesn't exist")

    for item in stock_dict:
        if stock_dict[item] > 0:
            print(f"{item} -> {stock_dict[item]}")


order_from_shop(exam_time, shopping_time)
