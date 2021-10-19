def type_list(arr):
    int_list=[]
    string_list=[]
    for x in arr:
        if isinstance(x, int) is True:
            int_list.append(x)
        elif isinstance(x, str) is True:
            string_list.append(x)
    
    if int_list and string_list:
        sum=0
        phrase=''
        for z in int_list:
            sum+=z
        for x in string_list:
            phrase+=x+' '
        print('The list you entered is a mixed list')
        print('Sum: ',sum)
        print('String: ',phrase)
        return True
    elif int_list and not string_list:
        sum=0
        for z in int_list:
            sum+=z
        print('The list you entered is of integer type')
        print('Sum: ',sum)
        return True 
    else:
        phrase=''
        for x in string_list:
            phrase+=x+' '
        print('The list you entered is of string type')
        print(phrase)
        return phrase
    
a=[1,2,3,4]
b=['Hi','my','name','is']
c=[1,2,'hello',3,'world']
d=[23,45,567,43,23]
e=['hello', 'I',2,34]
type_list(a)
type_list(b)
type_list(c)
type_list(d)
type_list(e)