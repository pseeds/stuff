def input_check(value):
    if (value >= 4 and value <= 10):
        return True
    else:
        return False


def check_list(input_list):
    if (len(input_list) < 1):
        return "EMPTY"
    else:
        return "NOT EMPTY"
        

def write_string_to_filename(file_name, str_value):
    f = open(file_name, "w+")
    f.write(str_value)
    f.close()
    
    
def list_double(i_list):
    new_list = []
    
    #if (len(i_list) < 1):
    #  return new_list   
    
    for val in i_list:
        n_val = val * 2
        new_list.append(n_val)
    
    return new_list


rv = input_check(3)
print rv
rv = input_check(4)
print rv
rv = input_check(10)
print rv
rv = input_check(11)
print rv


ilist = []
rv = check_list(ilist)
print rv

ilist.append("Dumb")
rv = check_list(ilist)
print rv

write_string_to_filename("test.txt", "abcdefg")

ilist = []
rv_list = list_double(ilist)
print rv_list

ilist.append(2)
ilist.append(25)
rv_list = list_double(ilist)
print rv_list
