import cgi, cgitb
import pandas 
# Create instance of FieldStorage
form = cgi.FieldStorage()
fnme=[]
lnme=[]
sub=[]
doubts=[]
f_name=form.getvalue("firstname")
l_name=form.getvalue("lastname")
subs=form.getvalue("subject")
dobt=form.getvalue("doubt")

fnme.append(f_name)
lnme.append(l_name)
sub.append(subs)
doubts.append(dobt)
dict={'first_name':fnme,"last_name":lnme,"subject":sub,"doubts":doubts}
df=pandas.DataFrame(dict)
df.to_csv('Doubts.csv')