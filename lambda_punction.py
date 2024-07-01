import json
import random
import pymysql

def lambda_handler(event, context):
    #tiny = event["queryStringParameters"]["tiny"]
    print({"event": event, "context":context})
    tiny = ""
    gen = ""
    content = ""
    lurl = ""
    turl = ""
    
    if event['queryStringParameters'].get('tiny'):
        tiny = event["queryStringParameters"]["tiny"]
    if event['queryStringParameters'].get('gen'):
        gen = event["queryStringParameters"]["gen"]
    if event['queryStringParameters'].get('lurl'):
        lurl = event["queryStringParameters"]["lurl"]

    print("tiny: " + tiny)    
    print("gen:" + gen)
    print("lurl:" + lurl)

    if len(tiny) == 5:
        #content = url
#        content = "<!DOCTYPE html> <html> <head> <meta http-equiv='Refresh' content='2; url=https://www.w3docs.com' /> </head> </html>"
        print(f"IfTinyTrue={tiny}")
        sqlreturn = sqlSelect(tiny)
        if sqlreturn == "":
            print(f"sqlreturn: {sqlreturn}")
        else:
            print(f"sqlreturn: {sqlreturn}")
            if "http" in sqlreturn:
                sqlreturn = sqlreturn.replace("http://","")
            if "https" in sqlreturn:
                sqlreturn = sqlreturn.replace("https://","")
            content = "<!DOCTYPE html> <html> <head> <meta http-equiv='Refresh' content='0; url=http://"+ sqlreturn +"' /> </head> </html>"
    
    if (len(gen) == 1):
        turl = generateUrl()
       # content = "tiny/?" +  turl
        content = "<p><a href=http://tiny/?" + turl + ">" + turl +"</a></html>"

        print(lurl)
        print(turl)
#        sqlSelect()
        sqlInsert(lurl,turl)
    
    if (len(tiny) != 5) & (gen == ""):
        content = "<html> TinyUrl generator<br><br><form method='GET' action='https://7kal7z2fppfawmne5qtgjus2du0zknld.lambda-url.eu-west-2.on.aws/'><label for='fname'>URL to be Converted:</label><br><input type='text' size='100' name='lurl'><input type='hidden' name='gen' value='1'><br><br><input type='submit' value='GO'></form>" + lurl

    return {"statusCode": 200, "headers": {'Content-Type': 'text/html'}, "body" : content
}

def myrandfunc():
    myrand = random.randint(0, 128)
    return myrand 
    
def fifi(x):
    if x >=48 | x <=57 | x >= 65 & x < 91 | x >= 97 | x <= 122:
        return x
    else:
        return 0

def generateUrl():
    count = 0
    url = ''

    while count<5:
       count+=1
       myrnd = myrandfunc()
 #      print("#" + str(count) + " " + " rnd:" + str(myrnd) + " chr: " + chr(myrnd))
  #     print(fifi(myrnd))
       if fifi(myrnd) == 0:
   #        print("not good")
           count = count - 1
       else:
    #    print("Good")
        url = url + str(chr(myrnd))
    return url


def sqlInsert(lUrl,tUrl):
    content = ""
    # Database connection parameters
    endpoint = 'database-1.cv40eksimxb2.eu-west-2.rds.amazonaws.com'
    username = 'admin'
    password = 'password'
    db_name = 'Tiny'
    
    # Establish a connection to the database
    connection = pymysql.connect(host=endpoint,user=username,password=password,database=db_name,connect_timeout=5)
    cursor = connection.cursor()
  
    cursor.execute(f"INSERT INTO TinyUrl (lUrl, tUrl) VALUES ('{lUrl}','{tUrl}');")
    connection.commit()
  
    cursor.close()
    connection.close()
    return {
        "statusCode": 200,
        "headers": {'Content-Type': 'text/html'},
        "body" : content
    }

def sqlSelect(tiny):
    content1 = ""
    # Database connection parameters
    endpoint = 'database-1.cv40eksimxb2.eu-west-2.rds.amazonaws.com'
    username = 'admin'
    password = 'password'
    db_name = 'Tiny'
    
    # Establish a connection to the database
    connection = pymysql.connect(host=endpoint,user=username,password=password,database=db_name,connect_timeout=5)
    cursor = connection.cursor()
    
    print(f"SqlSelectFuntion: {tiny}")
    #cursor.execute('select * from TinyUrl')
    cursor.execute(f"select * from TinyUrl where tUrl = '{tiny}'")
    rows = cursor.fetchall()
    number_of_rows = cursor.execute(f"select * from TinyUrl where tUrl = '{tiny}'")
    print(f"rows:{number_of_rows}")

    for row in rows:
        print(row[0] + " " + row[1])
        #content1 = content1 + (row[0] + " " + row[1] + "<br>")
        content1 = content1 + (row[0])

    cursor.close()
    connection.close()
    return content1
#    return {
 #       "statusCode": 200,
 #       "body" : content1
 #       "headers": {'Content-Type': 'text/html'},
#    }
