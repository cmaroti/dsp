
def read_file(csv_file_name):
    list_of_faculty = []
    with open(csv_file_name) as f:
        list_of_faculty = [line.rstrip('\n') for line in f]
    list_of_faculty = list(map(lambda x: x.split(','), list_of_faculty))
    del list_of_faculty[0]
    return list_of_faculty


def emails(list_of_faculty):
    list_of_emails = [x[3] for x in list_of_faculty]
    list_of_emails = [x.lower() for x in list_of_emails]
    return list_of_emails


def write_to_csv(list_of_emails):
    with open('emails.csv', 'w+') as f:
        f.write('list_of_emails\n')
        for email in list_of_emails:
            f.write(email+'\n')
            

faculty = read_file('faculty.csv')
email_list = emails(faculty)
write_to_csv(email_list)