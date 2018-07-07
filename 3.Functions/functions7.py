input_type = input()
value1 = input()
value2 = input()

def get_greater(int_t, v1, v2):
    result = None
    if in_t == 'int':
        if int(v1) > int(v2):
            result = v1
        elif int(v1) < int(v2):
            result =  v2
        else:
            result = v1

    elif int_t == 'char':
        if ord(v1) > ord(v2):
            result = v1
        elif ord(v1) < ord(v2):
            result = v2
        else:
            result = v1
    else:
        if v1 > v2:
            result = v1
        elif v1 < v2:
            result = v2
        else:
            result = v1

    return result

print(get_greater(input_type,value1,value2))
