import cgi, cgitb
import pandas 
# Create instance of FieldStorage
form = cgi.FieldStorage()
nme=[]
ps=[]

user_name=form.getvalue("username")
pass_word=form.getvalue("password")

nme.append(user_name)
ps.append(pass_word)

dict={'username':nme,"password":ps}
df=pandas.DataFrame(dict)
df.to_csv('login.csv')