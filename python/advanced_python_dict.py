
def read_file(csv_file_name):
    list_of_faculty = []
    with open(csv_file_name) as f:
        list_of_faculty = [line.rstrip('\n') for line in f]
    list_of_faculty = list(map(lambda x: x.split(','), list_of_faculty))
    del list_of_faculty[0]
    return list_of_faculty


def get_dict(list_of_faculty):
    new_dict = {}
    for item in list_of_faculty:
        lastname = item[0].split(' ')[-1]
        if lastname in new_dict.keys():
            new_dict[lastname].append(item[1:])
        else:
            new_dict[lastname] = []
            new_dict[lastname].append(item[1:])
    return new_dict
         
   
def get_dict2(list_of_faculty):
    new_dict = {}
    for item in list_of_faculty:
        name = tuple(item[0].split(' '))
        new_dict[name] = item[1:]
    return new_dict


faculty = read_file('faculty.csv')
print(get_dict(faculty),'\n')
print('By first name:')
faculty_list = get_dict2(faculty)
print({k: faculty_list[k] for k in sorted(faculty_list.keys())[0:3]},'\n')
print('By last name:')
newkeys = sorted(faculty_list.keys(), key=lambda x: x[-1])
print({k: faculty_list[k] for k in newkeys[0:3]})