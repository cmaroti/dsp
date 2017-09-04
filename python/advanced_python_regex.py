import pprint as pp

def read_file(csv_file_name):
    list_of_faculty = []
    with open(csv_file_name) as f:
        list_of_faculty = [line.rstrip('\n') for line in f]
    list_of_faculty = list(map(lambda x: x.split(','), list_of_faculty))
    del list_of_faculty[0]
    return list_of_faculty


def count_degs(list_of_faculty):
    list_of_degs = [x[1] for x in list_of_faculty]
    list_of_degs = [x.replace('.','') for x in list_of_degs]
    list_of_degs = [x.upper() for x in list_of_degs]
    list_of_degs = list(map(lambda x: x.split(' '), list_of_degs))
    list_of_degs = [x for y in list_of_degs for x in y]
    deg_count = {}
    for deg in list_of_degs:
        if deg == '':
            pass
        elif deg in deg_count.keys():
            deg_count[deg] += 1
        else:
            deg_count[deg] = 1
    return deg_count


def count_titles(list_of_faculty):
    list_of_titles = [x[2] for x in list_of_faculty]
    list_of_titles = [x.lower() for x in list_of_titles]
    list_of_titles = [x.split(' ') for x in list_of_titles]
    title_count = {}
    for title in list_of_titles:
        if title[0] in title_count.keys():
            title_count[title[0]] += 1
        else:
            title_count[title[0]] = 1
    return title_count


def emails(list_of_faculty):
    list_of_emails = [x[3] for x in list_of_faculty]
    list_of_emails = [x.lower() for x in list_of_emails]
    return list_of_emails


def unique_domains(emails):
    domains = set()
    for email in emails:
        index = email.find('@')
        domains.add(email[index+1:])
    return domains
            

faculty = read_file('faculty.csv')
pp.pprint(count_degs(faculty))
pp.pprint(count_titles(faculty))
email_list = emails(faculty)
pp.pprint(email_list)
pp.pprint(unique_domains(email_list))