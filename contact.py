import cgi, cgitb
import pandas 
# Create instance of FieldStorage
form = cgi.FieldStorage()
nme=[]
em=[]
nm=[]
th=[]
user_name=form.getvalue("username")
e_mail=form.getvalue("email")
num=form.getvalue("number")
thought=form.getvalue("thoughts")
nme.append(user_name)
em.append(e_mail)
nm.append(num)
th.append(thought)
dict={'username':nme,"email":em,"mobile number":nm,"Feedback":th}
df=pandas.DataFrame(dict)
df.to_csv('Contacts.csv')