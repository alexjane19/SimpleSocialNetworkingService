import psycopg2
'''
def create_db():
    con = psycopg2.connect(database='postgres', user='postgres', host='localhost', password='6665737')
    cur = con.cursor()
    cur.execute("create user alexjane with password '1234';")
    con.commit()
    cur.execute("create database kashangram2;")
    con.commit()
    cur.execute("grant all on database 'kashangram2' to alexjane;")
    con.commit()
    cur.close()
    con.close()
'''

_qurey_profile = '''CREATE TABLE profile
                    (
                      userid character varying(20) NOT NULL,
                      fname character varying(20),
                      lname character varying(20),
                      email character varying(40),
                      password text,
                      phonenumber character varying(14),
                      stno character varying(12),
                      photoid text,
                      date timestamp without time zone,
                      CONSTRAINT profile_pkey PRIMARY KEY (userid)
                    )'''

_qurey_photo = '''CREATE TABLE photo
                (
                  userid character varying(20),
                  photoid text NOT NULL,
                  writing text,
                  accesslevel boolean DEFAULT false,
                  date timestamp without time zone,
                  CONSTRAINT photo_pkey PRIMARY KEY (photoid),
                  CONSTRAINT profilephoto_fkey FOREIGN KEY (userid)
                      REFERENCES profile (userid) MATCH SIMPLE
                      ON UPDATE NO ACTION ON DELETE NO ACTION
                ) '''
_qurey_like = '''CREATE TABLE likes
                (
                  photoid text,
                  userid character varying(20),
                  date timestamp without time zone,
                  CONSTRAINT photolike_fkey FOREIGN KEY (photoid)
                      REFERENCES photo (photoid) MATCH SIMPLE
                      ON UPDATE NO ACTION ON DELETE NO ACTION
) '''
_qurey_comment = '''CREATE TABLE comment
                    (
                      userid character varying(20),
                      photoid text,
                      writing text,
                      date timestamp without time zone,
                      CONSTRAINT photocomment_fkey FOREIGN KEY (photoid)
                          REFERENCES photo (photoid) MATCH SIMPLE
                          ON UPDATE NO ACTION ON DELETE NO ACTION
                    ) '''
_qurey_tag = '''CREATE TABLE tag
                (
                  photoid text,
                  userid character varying(20),
                  date timestamp without time zone,
                  CONSTRAINT phototag_fkey FOREIGN KEY (photoid)
                      REFERENCES photo (photoid) MATCH SIMPLE
                      ON UPDATE NO ACTION ON DELETE NO ACTION
                ) '''
_qurey_follow = '''CREATE TABLE follow
                (
                  userid character varying(20),
                  fuserid character varying(20),
                  date timestamp without time zone,
                  CONSTRAINT profilefollow_fkey FOREIGN KEY (userid)
                      REFERENCES profile (userid) MATCH SIMPLE
                      ON UPDATE NO ACTION ON DELETE NO ACTION
                ) '''



def connection_database():
  conn=psycopg2.connect(database="kashangram2", user="alex", password="1234",host='127.0.0.1')
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

def main():

    db = qurey_in_database(_qurey_profile)
    close_database(db)
    db = qurey_in_database(_qurey_photo)
    close_database(db)
    db = qurey_in_database(_qurey_comment)
    close_database(db)
    db = qurey_in_database(_qurey_tag)
    close_database(db)
    db = qurey_in_database(_qurey_like)
    close_database(db)
    db = qurey_in_database(_qurey_follow)
    close_database(db)
    print("Create Tables Successful.")


if __name__ == '__main__':
    main()