def phonebook(names, numbers):
    dict = {}
    for i in range(0,len(names)):
        dict[names[i]] = numbers[i]
    return dict
name_list = ['Jackie', 'Joshua', 'Marguerite']
number_list = ['404-555-1234', '678-555-5678', '770-555-9012']
print(phonebook(name_list, number_list))