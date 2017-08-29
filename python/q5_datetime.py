# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

def difference_in_days(date1, date2):
    date1normal = datetime.strptime(date1, '%m-%d-%Y')
    date2normal = datetime.strptime(date2, '%m-%d-%Y')
    return (date2normal - date1normal).days

difference_in_days(date_start, date_stop)
# answer: 937 days

####b)  
date_start = '12312013'  
date_stop = '05282015'  

def difference_in_days(date1, date2):
    date1normal = datetime.strptime(date1, '%m%d%Y')
    date2normal = datetime.strptime(date2, '%m%d%Y')
    return (date2normal - date1normal).days

difference_in_days(date_start, date_stop)
# answer: 513 days
  
####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

def difference_in_days(date1, date2):
    date1normal = datetime.strptime(date1, '%d-%b-%Y')
    date2normal = datetime.strptime(date2, '%d-%b-%Y')
    return (date2normal - date1normal).days

difference_in_days(date_start, date_stop)
# answer: 7850 days
