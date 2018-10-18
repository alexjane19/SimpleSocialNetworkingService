import psycopg2
from time import gmtime, strftime
'''
conn = psycopg2.connect(database="kashangram", user="postgres", password="6665737",host='127.0.0.1')
cur = conn.cursor()
conn.commit();

s1=input('Enter a sno: ')
sname1=input('Enter sname ')

stmt1="insert into profile values('"+s1+"', '"+sname1+"' );"

cur.execute(stmt1)
'''
'''
cur.execute("insert into profile values('02','cilixcorp','cilix','corp','cilixcorp@gmail.com','alex123456789','25177','922','123456');")

conn.commit()
cur.execute("select * from profile;");
for a in cur.fetchall():
  for l1 in a:
    #print(l1,type(l1),end=' ');
    if type(l1) != int and type(l1)!=float and l1!=None:
      print(l1,end=' ');
  print()

cur.close()
conn.close()
'''


class Profile:
  def __init__(self,**_profile):
    self.profile=_profile

  def setUserId(self,_userId):
    self.profile['userid']=_userId
  def setFirstName(self,_firstName):
    self.profile['firstname']=_firstName
  def setLastName(self,_lastName):
    self.profile['lastname']=_lastName
  def setEmail(self,_email):
    self.profile['email']=_email
  def setPassWord(self,_password):
    self.profile['password']=_password
  def setPhoneNumber(self,_phoneNumber):
    self.profile['phonenumber']=_phoneNumber
  def setStudentNumber(self,_studentNumber):
    self.profile['stno']=_studentNumber
  def setPhotoId(self,_photoId):
    self.profile['photoid']=_photoId
  def setDate(self,_date):
    self.profile['date']=_date

  def getAll(self):
    return self.profile
  def getUserId(self):
    return self.profile['userid']
  def getFirstName(self):
     return self.profile['firstname']
  def getLastName(self):
    return self.profile['lastname']
  def getEmail(self):
    return self.profile['email']
  def getPassWord(self):
    return self.profile['password']
  def getPhoneNumber(self):
    return self.profile['phonenumber']
  def getStudentNumber(self,):
    return self.profile['stno']
  def getPhotoId(self):
    return self.profile['photoid']
  def getDate(self):
    return self.profile['date']

  def insert(self):
    self.profile['userid']=input('Username: ')
    self.profile['firstname']=input('First Name: ')
    self.profile['lastname']=input('Last Name: ')
    self.profile['email']=input('Email: ')
    self.profile['password']=input('Password: ')
    self.profile['phonenumber']=input('Phone Number: ')
    self.profile['stno']=input('Student Number: ')
    self.profile['photoid']=input('Photo: ')
    self.profile['date']=get_now_time()

  def update(self):
    _firstname = input("Edit First Name ({}): ".format(self.getFirstName()))
    if len(_firstname)>0:
      self.setFirstName(_firstname)
    _lastname = input("Edit Last Name ({}): ".format(self.getLastName()))
    if len(_lastname)>0:
      self.setLastName(_lastname)
    _email = input("Edit Email ({}): ".format(self.getEmail()))
    if len(_email)>0:
      self.setEmail(_email)
    _phonenumber = input("Edit Phone Number ({}): ".format(self.getPhoneNumber()))
    if len(_phonenumber)>0:
      self.setPhoneNumber(_phonenumber)
    _stno = input("Edit Student Number ({}): ".format(self.getStudentNumber()))
    if len(_stno)>0:
      self.setStudentNumber(_stno)
    _photoid = input("Edit Photo Id ({}): ".format(self.getPhotoId()))
    if len(_photoid)>0:
      self.setPhotoId(_photoid)


class Photo:
  def __init__(self,**photo):
    self.photo=photo

  def setUserId(self,_userId):
    self.photo['userid']=_userId
  def setPhotoId(self,_photoId):
    self.photo['photoid']=_photoId
  def setWriting(self,_writing):
    self.photo['writing']=_writing
  def setAccessLevel(self,_accessLevel):
    self.photo['accesslevel']=_accessLevel
  def setDate(self,_date):
    self.photo['date']=_date

  def getAll(self):
    return self.photo
  def getUserId(self):
    return self.photo['userid']
  def getPhotoId(self):
     return self.photo['photoid']
  def getWriting(self):
    return self.photo['writing']
  def getAccessLevel(self):
    return self.photo['accesslevel']
  def getDate(self):
    return self.photo['date']

  def insert(self,_username):
    self.photo['userid']=_username
    self.photo['photoid']=input('Enter a photo id: ')
    self.photo['writing']=input('Writing a text: ')
    _sel=eval(input('Select access level (1.Private/2.Public): '))
    if(_sel==1):
      self.photo['accesslevel']='0'
    else:
      self.photo['accesslevel']='1'
    self.photo['date']=get_now_time()

  def update(self):
    _photoid = input("Edit this photoId ({}): ".format(self.getPhotoId()))
    if len(_photoid)>0:
      self.setPhotoId(_photoid)
    _writing = input("Edit this writing ({}): ".format(self.getWriting()))
    if len(_writing)>0:
      self.setWriting(_writing)
    _sel=eval(input('Edit access level (1.Private/2.Public): '))
    if  len(str(_sel))>0:
      if(_sel==1):
        self.photo['accesslevel']='0'
      else:
        self.photo['accesslevel']='1'


class Like:
  def __init__(self,**like):
    self.like=like

  def setUserId(self,_userId):
    self.like['userid']=_userId
  def setPhotoId(self,_photoId):
    self.like['photoid']=_photoId
  def setDate(self,_date):
    self.like['date']=_date

  def getAll(self):
    return self.like
  def getUserId(self):
    return self.like['userid']
  def getPhotoId(self):
     return self.like['photoid']
  def getDate(self):
    return self.like['date']
  def insert(self,_username,_photoid):
    self.setUserId(_username)
    self.setPhotoId(_photoid)
    self.setDate(get_now_time())


class Comment:
  def __init__(self,**comment):
    self.comment=comment

  def setUserId(self,_userId):
    self.comment['userid']=_userId
  def setPhotoId(self,_photoId):
    self.comment['photoid']=_photoId
  def setWriting(self,_writing):
    self.comment['writing']=_writing
  def setDate(self,_date):
    self.comment['date']=_date

  def getAll(self):
    return self.comment
  def getUserId(self):
    return self.comment['userid']
  def getPhotoId(self):
     return self.comment['photoid']
  def getWriting(self):
    return self.comment['writing']
  def getDate(self):
    return self.comment['date']

  def insert(self,_username,_photoiid):
    self.setUserId(_username)
    self.setPhotoId(_photoiid)
    self.comment['writing']=input("Write a comment: ")
    self.setDate(get_now_time())

  def update(self):
    _writing = input("Edit comment ({}): ".format(self.getWriting()))
    if len(_writing)>0:
      self.setWriting(_writing)
      self.setDate(get_now_time())


class Tag:
  def __init__(self,**tag):
    self.tag=tag

  def setUserId(self,_userId):
    self.tag['userid']=_userId
  def setPhotoId(self,_photoId):
    self.tag['photoid']=_photoId
  def setDate(self,_date):
    self.tag['date']=_date

  def getAll(self):
    return self.tag
  def getUserId(self):
    return self.tag['userid']
  def getPhotoId(self):
     return self.tag['photoid']
  def getDate(self):
    return self.tag['date']

  def insert(self,_username,_photoid):
    self.setUserId(_username)
    self.setPhotoId(_photoid)
    self.setDate(get_now_time())


class Follow:
  def __init__(self,**follow):
    self.follow=follow

  def setUserId(self,_userId):
    self.follow['userid']=_userId
  def setFollowUserId(self,_followUserId):
    self.follow['followuserid']=_followUserId
  def setDate(self,_date):
    self.follow['date']=_date

  def getAll(self):
    return self.follow
  def getUserId(self):
    return self.follow['userid']
  def getFollowUserId(self):
     return self.follow['followuserid']
  def getDate(self):
    return self.follow['date']

  def insert(self,_userid,_followuserid):
    self.setUserId(_userid)
    self.setFollowUserId(_followuserid)
    self.setDate(get_now_time())


def get_now_time():
  return strftime("%Y-%m-%d %H:%M:%S", gmtime())


def connection_database():
  conn=psycopg2.connect(database="kashangram", user="postgres", password="6665737",host='127.0.0.1')
  cur=conn.cursor()
  return {'connection':conn, 'cursor':cur}


def qurey_in_database(qurey):
  db=connection_database()
  db['cursor'].execute(qurey)
  db['connection'].commit()
  return db


def close_database(db):
  db['cursor'].close()
  db['connection'].close()


def check_signup(_userid):
  _qurey="select userid from profile where userid='"+_userid+"';"
  db = qurey_in_database(_qurey)
  try:
    if db['cursor'].fetchone()[0]==_userid:
      close_database(db)
      return False
  except TypeError as e:
    close_database(db)
    return True


def signup():
  print("Signup:\n")
  _person=Profile()
  _person.insert()
  if check_signup(_person.getUserId()):
    _qurey="insert into profile values('"+_person.getUserId()+"', '"+_person.getFirstName()+"', '"+_person.getLastName()+"', '"+_person.getEmail()+"', '"\
         +_person.getPassWord()+"', '"+_person.getPhoneNumber()+"', '"+_person.getStudentNumber()+"', '"+_person.getPhotoId()+"', '"+_person.getDate()+"' );"
    db=qurey_in_database(_qurey)
    close_database(db)
    print("\nRegistration was successful.")
  else:
    print("\nThis user already registered.")


def login():
  print("Login:\n")
  _userid = input("Username: ")
  _pass = input("Password: ")
  _qurey="select * from profile where password='"+_pass+"' and userid='"+_userid+"';"
  db = qurey_in_database(_qurey)
  _temp=db['cursor'].fetchone()
  if _temp== None:
    print("\nUsername or password is wrong.")
    _sel=input("do you forget your password?(y/n) ")
    if(_sel=='y'):
      forget_password()
  else:
    _person = Profile(userid = _temp[0], firstname = _temp[1], lastname = _temp[2], email = _temp[3], password = _temp[4],
                      phonenumber = _temp[5], stno =_temp[6], photoid = _temp[7], date=_temp[8])
    print("Login successful.")
  close_database(db)
  return _person


def forget_password():
  print("Forget Password:\n")
  _username = input("Username: ")
  _phoneNumber = input("Phone Number: ")
  _password1 = input("New password: ")
  _password2 = input("Retry new password: ")
  if _password1==_password2:
    _qurey = "update profile set password='"+_password1+"' where userid='"+_username+"' and phonenumber='"+_phoneNumber+"';"
    db = qurey_in_database(_qurey)
    print("Password is changed.")
    close_database(db)
  else:
    print("No match new password and retry new password.")


def edit_profile(_person):
  print("Edit Profile\'s {}:\n".format(_person.getUserId()))
  _person.update()
  _qurey = "update profile set photoid='"+_person.getPhotoId()+"', fname='"+_person.getFirstName()+"', lname='"\
           +_person.getLastName()+"', email='"+_person.getEmail()+"', phonenumber='"+_person.getPhoneNumber()+"', stno='"\
           +_person.getStudentNumber()+"', photoid='"+_person.getPhotoId()+"' where userid='"+_person.getUserId()+"';"
  db = qurey_in_database(_qurey)
  close_database(db)


def share_user_photo(_person):
  _photo = Photo()
  _photo.insert(_person.getUserId())
  _qurey = "insert into photo values('"+_photo.getUserId()+"', '"+_photo.getPhotoId()+"', '"+_photo.getWriting()+"', '"\
           +_photo.getAccessLevel()+"', '"+_photo.getDate()+"');"
  db = qurey_in_database(_qurey)
  close_database(db)


def get_all_user_photo(_person):
  _qurey="select * from photo where userid='"+_person.getUserId()+"';"
  db = qurey_in_database(_qurey)
  _index=0
  _photo=[]
  for a in db['cursor'].fetchall():
    _photo.append(Photo(userid = a[0], photoid = a[1], writing = a[2], accesslevel = a[3], date = a[4]))
    for l1 in a:
      print(l1, end=' ');
    print("")
    _index+=1
  close_database(db)
  return _photo;


def edit_user_photo(_photo):
  _prephotoid = _photo.getPhotoId()
  _photo.update()
  _qurey = "update photo set photoid='"+_photo.getPhotoId()+"', writing='"+_photo.getWriting()+"', accesslevel='"\
           +_photo.getAccessLevel()+"' where photoid='"+_prephotoid+"';"
  db = qurey_in_database(_qurey)
  close_database(db)


def delete_user_photo(_photo):
  _qurey = "delete from photo where photoid = '"+_photo.getPhotoId()+"';"
  db = qurey_in_database(_qurey)
  close_database(db)
  del _photo


def like_a_photo(_person,_photo):
  _like = Like()
  _like.insert(_person.getUserId(),_photo.getPhotoId())
  _qurey = "insert into likes values('"+_like.getPhotoId()+"', '"+_like.getUserId()+"', '"+_like.getDate()+"' );"
  db = qurey_in_database(_qurey)
  close_database(db)

def get_like_a_photo(_photo):
  _qurey="select * from likes where photoid='"+_photo.getPhotoId()+"';"
  db = qurey_in_database(_qurey)
  _index=0
  _like=[]
  for a in db['cursor'].fetchall():
    _like.append(Like(photoid = a[0], userid = a[1], date = a[2]))
    for l1 in a:
      print(l1, end=' ');
    print("")
    _index+=1
  close_database(db)
  return _like;


def dislike_a_photo(_like):
  _qurey = "delete from likes where photoid = '"+_like.getPhotoId()+"' and userid = '"+_like.getUserId()+"';"
  db = qurey_in_database(_qurey)
  close_database(db)
  del _like


def comment_a_photo(_person,_photo):
  _comment = Comment()
  _comment.insert(_person.getUserId(),_photo.getPhotoId())
  _qurey = "insert into comment values('"+_comment.getPhotoId()+"', '"+_comment.getUserId()+"', '"+_comment.getWriting()+"', '"+_comment.getDate()+"');"
  db = qurey_in_database(_qurey)
  close_database(db)


def get_comment_a_photo(_photo):
  _qurey="select * from comment where photoid='"+_photo.getPhotoId()+"';"
  db = qurey_in_database(_qurey)
  _index=0
  _comment=[]
  for a in db['cursor'].fetchall():
    _comment.append(Comment(photoid = a[0], userid = a[1], writing = a[2], date = a[3]))
    for l1 in a:
      print(l1, end=' ');
    print("")
    _index+=1
  close_database(db)
  return _comment;


def edit_comment_a_photo(_comment):
  _comment.update()
  _qurey = "update comment set writing='"+_comment.getWriting()+"', date='"+_comment.getDate()+\
           "' where photoid = '"+_comment.getPhotoId()+"' and userid = '"+_comment.getUserId()+"';"
  db = qurey_in_database(_qurey)
  close_database(db)


def delete_comment_photo(_comment):
  _qurey = "delete from comment where photoid = '"+_comment.getPhotoId()+"' and userid = '"+_comment.getUserId()+"';"
  db = qurey_in_database(_qurey)
  close_database(db)
  del _comment


def tag_a_photo(_person,_photo):
  _tag = Tag()
  _tag.insert(_person.getUserId(),_photo.getPhotoId())
  _qurey = "insert into tag values('"+_tag.getPhotoId()+"', '"+_tag.getUserId()+"', '"+_tag.getDate()+"');"
  db = qurey_in_database(_qurey)
  close_database(db)


def get_tag_a_photo(_photo):
  _qurey="select * from tag where photoid='"+_photo.getPhotoId()+"';"
  db = qurey_in_database(_qurey)
  _index=0
  _tag=[]
  for a in db['cursor'].fetchall():
    _tag.append(Tag(photoid = a[0], userid = a[1], date = a[2]))
    for l1 in a:
      print(l1, end=' ');
    print("")
    _index+=1
  close_database(db)
  return _tag;


def untag_a_photo(_tag):
  _qurey = "delete from tag where photoid = '"+_tag.getPhotoId()+"' and userid = '"+_tag.getUserId()+"';"
  db = qurey_in_database(_qurey)
  close_database(db)
  del _tag


def following(_person,_f_person):
  _following = Follow()
  _following.insert(_person.getUserId(),_f_person.getUserId)
  _qurey = "insert into follow values('"+_following.getUserId()+"', '"+_following.getFollowUserId()+"', '"+_following.getDate()+"');"
  db = qurey_in_database(_qurey)
  close_database(db)


def get_following(_person):
  _qurey="select * from follow where userid='"+_person.getUserId()+"';"
  db = qurey_in_database(_qurey)
  _index=0
  _following=[]
  for a in db['cursor'].fetchall():
    _following.append(Follow(userid = a[0], followuserid = a[1], date = a[2]))
    for l1 in a:
      print(l1, end=' ');
    print("")
    _index+=1
  close_database(db)
  return _following;


def get_followers(_person):
  _qurey="select * from follow where fuserid='"+_person.getUserId()+"';"
  db = qurey_in_database(_qurey)
  _index=0
  _followers=[]
  for a in db['cursor'].fetchall():
    _followers.append(Follow(userid = a[0], followuserid = a[1], date = a[2]))
    for l1 in a:
      print(l1, end=' ');
    print("")
    _index+=1
  close_database(db)
  return _followers;


def unfollow(_follow):
  _qurey = "delete from follow where userid = '"+_follow.getUserId()+"' and fuserid = '"+_follow.getFollowUserId()+"';"
  db = qurey_in_database(_qurey)
  close_database(db)
  del _follow





''' ////important for list and dictionary
  _index=0
  _myphotos={}
  _photo=[]
  for a in db['cursor'].fetchall():
    _p = Photo(userid = a[0], photoid = a[1], writing = a[2], accesslevel = a[3], date = a[4])
    _photo.append([_p.getUserId(),_p.getPhotoId(),_p.getWriting()])
    for l1 in a:
      print(l1, end=' ');
    print("")
    _index+=1

  print(_photo[0])
  _myphotos[a[0]]=_photo
  close_database(db)
  print(_myphotos)
'''


def main():
  _choose = eval(input("1.Login\n2.Signup\n"))
  if(_choose==1):
    _person=login()
  if(_choose==2):
    signup()
  '''share_user_post(_person)'''
  _photo = get_all_user_photo(_person)

  '''
  _sel = input("select a photo for edit: ")
  for i in _photo:
    if i.getPhotoId()==_sel:
      _temp = i
 edit_user_photo(_temp)
  _sel = input("select a photo for delete: ")
  for i in _photo:
    if i.getPhotoId()==_sel:
      _temp = i

  delete_user_photo(_temp)
'''
  _sel = input("select a photo for like: ")
  for i in _photo:
    if i.getPhotoId()==_sel:
      _temp = i

  like_a_photo(_person,_temp)

  _like=get_like_a_photo(_temp)

  dislike_a_photo(_like[0])

if __name__ == "__main__": main()