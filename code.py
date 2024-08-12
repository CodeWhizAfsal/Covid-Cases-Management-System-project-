import mysql.connector as m
import time
con=m.connect(host="localhost",user="root",passwd="student",database="covid")

# For Creating tables in database
def crtTable():
    try:

# Creating table CCMS (All Details)
        cur=con.cursor()
        cur.execute("create table  CCMS (aadhaar bigint(15) primary key,\
                                     name varchar(20),\
                                     age int(3),\
                                     gender varchar(1),\
                                     localbody varchar(30),\
                                     district varchar(20),\
                                     testdt date,\
                                     resultdt date,\
                                     result varchar(10),\
                                     Status varchar(10) default 'ALIVE',\
                                     deathdt date)")
        con.commit()

# Creating table DCMS ( Positive case Details)       
        cur=con.cursor()
        cur.execute("create table  TPMS (aadhaar bigint(15) primary key,\
                                     name varchar(20),\
                                     age int(3),\
                                     gender varchar(1),\
                                     localbody varchar(30),\
                                     district varchar(20),\
                                     testdt date,\
                                     resultdt date,\
                                     result varchar(10),\
                                     Status varchar(10) default 'ALIVE',\
                                     deathdt date)")
        con.commit()

# Creating table DPMS (All death case Details)        
        cur=con.cursor()
        cur.execute("create table  DCMS (aadhaar bigint(15) primary key,\
                                     name varchar(20),\
                                     age int(3),\
                                     gender varchar(1),\
                                     localbody varchar(30),\
                                     district varchar(20),\
                                     testdt date,\
                                     resultdt date,\
                                     result varchar(10),\
                                     Status varchar(10) default 'Dead',\
                                     deathdt date)")
        con.commit()

# Creating table DPMS (Positive death case Details)        
        cur=con.cursor()
        cur.execute("create table  DPMS (aadhaar bigint(15) primary key,\
                                     name varchar(20),\
                                     age int(3),\
                                     gender varchar(1),\
                                     localbody varchar(30),\
                                     district varchar(20),\
                                     testdt date,\
                                     resultdt date,\
                                     result varchar(10),\
                                     Status varchar(10) default 'Dead',\
                                     deathdt date)")
        con.commit()
    except:
        pass
crtTable()

# For inputing new cases
def insert():
    b="Yy"
    while b in "Yy":
        aadhaar=input("Enter Aadhaar ID : ")
        if len(aadhaar)!=12:
            print ('Invalid Aadhaar')
            break
        name=input("Enter Name : ")
        q=''
        try:
           b=int(name)
        except:
           q='yeah'
        if q!='yeah':
             print('Wrong syntax')
             break
        try:
            idea=int(input('Enter Age : '))
            age=str(idea)
        except:
            print('Wrong syntax')
            break
        gender=input("Enter Gender : ")
        q=''
        try:
           b=int(gender)
        except:
           q='yeah'
        if q!='yeah':
          print('Wrong syntax')
          break
        localbody=input("Enter Local Body : ")
        q=''
        try:
           b=int(localbody)
        except:
           q='yeah'
        if q!='yeah':
          print('Wrong syntax')
          break
        district=input("Enter District : ")
        q=''
        try:
           b=int(district)
        except:
           q='yeah'
        if q!='yeah':
          print('Wrong syntax')
          break
        testdt=input("Enter Date of Test Taken (YYYY-MM-DD) : ")
        import time
        try:
            date ='2000-05-08'
            formatted_date1 = time.strptime(date, "%Y-%m-%d")
            formatted_date2 = time.strptime(testdt, "%Y-%m-%d")
        except:
            print('Wrong Syntax')
            break
        resultdt=input("Enter Date of Test Result Processed (YYYY-MM-DD) : ")
        import time
        try:
            date ='2000-05-08'
            formatted_date1 = time.strptime(date, "%Y-%m-%d")
            formatted_date2 = time.strptime(resultdt, "%Y-%m-%d")
        except:
            print('Wrong Syntax')
            break
        result=input("Enter Covid Test Result (POSITIVE/NEGATIVE) : ")
        try:           
            cur=con.cursor()
            qry="insert into CCMS(aadhaar,name,age,gender,localbody,district,testdt,resultdt,result) values(%s,%s,%s,%s,\
                                                                                                 %s,%s,%s,%s,%s)"
                                                                                           
            val=(aadhaar,name.capitalize(),age,gender.capitalize(),localbody.capitalize(),district.capitalize(),testdt,resultdt,result.upper())
            cur.execute(qry,val)
            con.commit()
            if result.upper()=="POSITIVE":
                qry="insert into TPMS(aadhaar,name,age,gender,localbody,district,testdt,resultdt,result) values(%s,%s,%s,%s,\
                                                                                                          %s,%s,%s,%s,%s)"
                val=(aadhaar,name.capitalize(),age,gender.capitalize(),localbody.capitalize(),district.capitalize(),testdt,resultdt,result.upper())
                cur.execute(qry,val)
                con.commit()
        except:
            print("The details were entered using an incorrect format")
        b=input("Do You Want to Add more Records If yes 'Y' else 'N' : ")

# For inputing death cases
def dead():
    b="Yy"
    while b in "Yy":
        cur=con.cursor()
        aadhaar=input("Enter Aadhaar ID : ")
        if len(aadhaar)!=12:
            print ('Invalid Aadhaar')
            break
        name=input("Enter Name : ")
        q=''
        try:
           b=int(name)
        except:
           q='yeah'
        if q!='yeah':
             print('Wrong syntax')
             break
        try:
            idea=int(input('Enter Age : '))
            age=str(idea)
        except:
            print('Wrong syntax')
            break
        gender=input("Enter Gender : ")
        q=''
        try:
           b=int(gender)
        except:
           q='yeah'
        if q!='yeah':
          print('Wrong syntax')
          break
        localbody=input("Enter Local Body : ")
        q=''
        try:
           b=int(localbody)
        except:
           q='yeah'
        if q!='yeah':
          print('Wrong syntax')
          break
        district=input("Enter District : ")
        q=''
        try:
           b=int(district)
        except:
           q='yeah'
        if q!='yeah':
          print('Wrong syntax')
          break
        testdt=input("Enter Date of Test Taken (YYYY-MM-DD) : ")
        import time
        try:
            date ='2000-05-08'
            formatted_date1 = time.strptime(date, "%Y-%m-%d")
            formatted_date2 = time.strptime(testdt, "%Y-%m-%d")
        except:
            print('Wrong Syntax')
            break
        deathdt=input("Enter Date of Death (YYYY-MM-DD) : ")
        import time
        try:
            date ='2000-05-08'
            formatted_date1 = time.strptime(date, "%Y-%m-%d")
            formatted_date2 = time.strptime(deathdt, "%Y-%m-%d")
        except:
            print('Wrong Syntax')          
        resultdt=input("Enter Date of Result Processed (YYYY-MM-DD) : ")
        import time
        try:
            date ='2000-05-08'
            formatted_date1 = time.strptime(date, "%Y-%m-%d")
            formatted_date2 = time.strptime(resultdt, "%Y-%m-%d")
        except:
            print('Wrong Syntax')
            break
        result=input("Enter Result of Covid Test (POSITIVE/NEGATIVE) : ")
        try:
            qry="insert into DCMS(aadhaar,name,age,gender,localbody,district,testdt,resultdt,result,deathdt) values(%s,%s,\
                                                                                                 %s,%s,%s,%s,%s,%s,%s,%s)"
            val=(aadhaar,name.capitalize(),age,gender.capitalize(),localbody.capitalize(),district.capitalize(),testdt,resultdt,result.upper(),deathdt)
            cur.execute(qry,val)
            con.commit()
            if result.upper()=="POSITIVE":
                qry="insert into DPMS(aadhaar,name,age,gender,localbody,district,testdt,resultdt,result,deathdt) values(%s,%s,\
                                                                                                   %s,%s,%s,%s,%s,%s,%s,%s)"
                val=(aadhaar,name.capitalize(),age,gender.capitalize(),localbody.capitalize(),district.capitalize(),testdt,resultdt,result.upper(),deathdt)
                cur.execute(qry,val)
                con.commit()
        except:
            print("The details entered use an incorrect format.")
        b=input("Do You Want to Add more Records If yes 'Y' else 'N' - ")

# for searching data using aadhar number            
def search():
    ad=input("Enter the Aadhaar ID of the person to be searched : ")
    if len(ad)!=12:
        print ('Invalid Aadhaar Number')
    else:
        try:
            while True:
                cur=con.cursor()
                qry="(select* from ccms where aadhaar = '{}' ) union (select* from dcms where aadhaar = '{}')".format(ad,ad)
                cur.execute(qry)
                s=cur.fetchall()
                for i in s:
                    a=[]
                    for j in i:
                        a.append(str(j))
                if a!=[]:
                    print("="*130)
                    print("{:<15}{:<15}{:<5}{:<7}{:<15}{:<15}{:<15}{:<15}{:<10}{:<8}{:<10}".format("Aadhaar", "Name","Age","Gender",\
                                                                             "Localbody","District","Testdt",\
                                                                             "Resultdt","Result","Status","Deathdt"))
                    print("="*130)
                    
                    
                print("{:<15}{:<10}{:<15}{:<7}{:<15}{:<15}{:<15}{:<15}{:<10}{:<8}{:<10}".format(a[0],a[1],a[2],a[3],a[4],\
                                                                                     a[5],a[6],a[7],a[8],a[9],a[10]))
                print("="*130)
                con.commit()
                break
        except:
            print("Aadhaar Id does not match any existing entries")

#for showing all the details entered till date    
def details():
    print("="*140)
    print("{:<15}{:<12}{:<15}{:<7}{:<15}{:<15}{:<15}{:<15}{:<10}{:<8}{:<10}".format("Aadhaar","Name","Age","Gender",\
                                                                             "Localbody","District","Testdt",\
                                                                             "Resultdt","Result","Status","Deathdt"))
    print("="*140)
    cur=con.cursor()
    qry="(select* from ccms  order by resultdt) "
    cur.execute(qry)
    s=cur.fetchall()
    con.commit()
    for i in s:
        a=[]
        for j in i:
            a.append(str(j))
        print("{:<15}{:<12}{:<15}{:<7}{:<15}{:<15}{:<15}{:<15}{:<10}{:<8}{:<10}".format(a[0],a[1],a[2],a[3],a[4],\
                                                                                 a[5],a[6],a[7],a[8],a[9],a[10]))
    qry="(select* from dcms order by resultdt ) "
    cur.execute(qry)
    s=cur.fetchall()
    con.commit()
    for i in s:
        a=[]
        for j in i:
            a.append(str(j))
        print("{:<15}{:<12}{:<15}{:<7}{:<15}{:<15}{:<15}{:<15}{:<10}{:<8}{:<10}".format(a[0],a[1],a[2],a[3],a[4],\
                                                                                 a[5],a[6],a[7],a[8],a[9],a[10]))

    print("="*140)

# For showing all the data regarding death cases    
def deathdetails():
    print("="*140)
    print("{:<15}{:<12}{:<5}{:<7}{:<15}{:<15}{:<15}{:<15}{:<10}{:<8}{:<10}".format("Aadhaar", "Name","Age","Gender",\
                                                                             "Localbody","District","Testdt",\
                                                                             "Resultdt","Result","Status","Deathdt"))
    print("="*140)
    cur=con.cursor()
    qry="(select* from ccms where status='dead' order by resultdt) "
    cur.execute(qry)
    s=cur.fetchall()
    con.commit()
    for i in s:
        a=[]
        for j in i:
            a.append(str(j))
        print("{:<15}{:<12}{:<5}{:<7}{:<15}{:<15}{:<15}{:<15}{:<10}{:<8}{:<10}".format(a[0],a[1],a[2],a[3],a[4],\
                                                                                 a[5],a[6],a[7],a[8],a[9],a[10]))
    qry="(select* from dpms order by resultdt) "
    cur.execute(qry)
    s=cur.fetchall()
    con.commit()
    for i in s:
        a=[]
        for j in i:
            a.append(str(j))
        print("{:<15}{:<12}{:<5}{:<7}{:<15}{:<15}{:<15}{:<15}{:<10}{:<8}{:<10}".format(a[0],a[1],a[2],a[3],a[4],\
                                                                                 a[5],a[6],a[7],a[8],a[9],a[10]))
    print("="*140)
# for updating the presemt condition  of a already existing record    
def update():
    x='t'
    while x=='t':
      mc=con.cursor()
      mc.execute("select aadhaar from ccms ")
      c=[]
      for x in mc:
          for i in x:
              c.append(str(i))
      ad=input("Enter the Aadhaar ID of the person to be updated : ")
      if len(ad)!=12:
        print ('Invalid Aadhaar Number')
      elif ad in c:
        try:
            cur=con.cursor()
            if len(ad)!=12:
                print ('Invalid Aadhaar Number')
            else:    
                inp=input("Enter the person whether alive or dead: ")
                ps=input("Covid Status : ")
                qry="update ccms set status='{}'where aadhaar = '{}'".format(inp.upper(),ad)
                cur.execute(qry)
                con.commit()
                qry="update ccms set result='{}'where aadhaar = '{}'".format(ps.upper(),ad)
                cur.execute(qry)
                if inp.upper()=="DEAD":
                    dt=input("enter Death Date (YYYY/MM/DD) : ")
                    qry="update ccms set deathdt='{}'where aadhaar = '{}'".format(dt,ad)
                    cur.execute(qry)
                    con.commit()
                con.commit()
                print("Data updated Successfully")
        except:
            print("entered Aadhaar not present in the records")
      else:
         print("Aadhaar Id does not match any existing entries")
# For showing all the active positive cases  
def active():
    print("="*120)
    print("{:<15}{:<15}{:<5}{:<7}{:<15}{:<15}{:<15}{:<15}{:<10}{:<8}".format("Aadhaar", "Name","Age","Gender","Localbody","district","testdt","resultdt","result","status"))
    print("="*120)
    cur=con.cursor()
    qry="select* from ccms  where result = 'POSITIVE' AND STATUS = 'ALIVE' order by resultdt"
    cur.execute(qry)
    s=cur.fetchall()
    for i in s:
        a=[]
        for j in i:
            a.append(str(j))
        print("{:<15}{:<15}{:<5}{:<7}{:<15}{:<15}{:<15}{:<15}{:<10}{:<8}".format(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9]))

    print("="*120)
    con.commit()

#for displaying district related information    
def district():
    ad=input("Enter District Name : ")
    ex="y"
    try:
        cur=con.cursor()
        con.commit()
        qry="select count(*) from tpms where district ='{}'".format(ad)
        cur.execute(qry)
        a=cur.fetchall()
        a=a[0][0]
        con.commit()
        qry="select count(*) from ccms where district ='{}' and result='POSITIVE' and deathdt IS null ".format(ad)
        cur.execute(qry)
        b=cur.fetchall()
        b=b[0][0]
        con.commit()
        qry="select count(*) from ccms where status = 'Dead' and district='{}'".format(ad)
        cur.execute(qry)
        d=cur.fetchall()
        d=d[0][0]
        con.commit()
        qry="select count(*) from ccms where district ='{}'".format(ad)
        cur.execute(qry)
        c=cur.fetchall()
        c=c[0][0]
        con.commit()
        qry="select count(*) from dpms where district ='{}'".format(ad)
        cur.execute(qry)
        k=cur.fetchall()
        k=k[0][0]
        con.commit()
        qry="select count(*) from dcms where district ='{}'".format(ad)
        cur.execute(qry)
        r=cur.fetchall()
        r=r[0][0]
        t=(a/c)*100
    except:
        print("\nThe given District does not exist")
        ex="n"
    while ex in "Yy":
        print("="*50)
        print("\t","\t","District Wise Statistics")
        print("="*50)
        print("1. Total Test taken ")
        print("2. Total Cases")
        print("3. Active Cases present")
        print("4. Total recovered")
        print("5. Total deaths")
        print("6. Test Positivity Ratio (TPR) ")
        print("7. Exit")
        choice=int(input("\n  Enter the option number to get the required service :"))
        print("="*50)
        print("                    ",ad,"   ")
        print("="*50)
        if choice==1:
            print("‣Total Tested",c+r)
        elif choice==2:
            print("‣Total cases",a+k) 
        elif choice==3:
            print("‣Total  active cases present",b)
        elif choice==4:
            print("‣Total recovered",a-(b+d))
        elif choice==5:
            print("‣Total deaths",d+k)
        elif choice==6:
            print("‣Test Positivity Rate",round(t,2))
        else :
            print('Enter Valid Option Number..')
        ex=input(" \n Do You Want to Continue District wise Statistics ,if Yes 'Y' else 'N' - ")

#for displaying localbody related information
def localbody():
    ad=input("enter Local Body : ")
    ex="y"
    try:
        cur=con.cursor()
        qry="select count(*) from tpms where localbody ='{}'".format(ad)
        cur.execute(qry)
        a=cur.fetchall()
        a=a[0][0]
        con.commit()
        qry="select count(*) from ccms where localbody ='{}' and result='POSITIVE' and deathdt  IS null ".format(ad)
        cur.execute(qry)
        b=cur.fetchall()
        b=b[0][0]
        con.commit()
        qry="select count(*) from ccms where status = 'Dead' and localbody='{}'".format(ad)
        cur.execute(qry)
        d=cur.fetchall()
        d=d[0][0]
        con.commit()
        qry="select count(*) from ccms where localbody ='{}'".format(ad)
        cur.execute(qry)
        c=cur.fetchall()
        c=c[0][0]
        con.commit()
        qry="select count(*) from dpms where localbody ='{}'".format(ad)
        cur.execute(qry)
        k=cur.fetchall()
        k=k[0][0]
        qry="select count(*) from dcms where localbody ='{}'".format(ad)
        cur.execute(qry)
        r=cur.fetchall()
        r=r[0][0]
        con.commit()
        t=(a/c)*100
        print("="*50)
    except:
        print("The given Local body does not exist")
        ex="n"
    while ex in "Yy":
        print("="*50)
        print("\t","\t","Local Body Wise Statistics")
        print("="*50)
        print("1. Total Test taken ")
        print("2. Total Cases")
        print("3. Active Cases present")
        print("4. Total recoverd")
        print("5. Total deaths")
        print("6. Test Positivity Ratio (TPR) ")
        print("7. Exit")
        choice=int(input("\n  Enter the option number to get the required service : "))
        print("="*50)
        print("                    ",ad,"   ")
        print("="*50)
        if choice==1:
            print("‣Total Tested",c+r)
        elif choice==2:
            print("‣Total cases",a+k) 
        elif choice==3:
            print("‣Total  active cases present",b)
        elif choice==4:
            print("‣Total recovered",a-(b+d))
        elif choice==5:
            print("‣Total deaths",d+k)
        elif choice==6:
            print("‣Test Positivity Rate",round(t,2))
        ex=input(" \n Do You Want to Continue Local Body  wise Statistics ,if Yes 'Y' else 'N' - ")
# for displaing age related information
def age():
    print("="*50)
    print("\t","\t","Age Wise Satistics")
    print("="*50)
    print("1. below 18 yrs")
    print("2. 18-45 yrs")
    print("3. 45-60 yrs")
    print("4. above 60 yrs")
    print("="*50)
    choice=int(input("Enter the option number to get the required service : "))
    if choice==1:
        f=0
        l=18
    elif choice==2:
        f=18
        l=45
    elif choice==3:
        f=45
        l=60
    elif choice==4:
        f=60
        l=100
    else:
        print('Option number',choice,' doesn’t exist') 
    cur=con.cursor()
    qry="select COUNT(*) from tpms where age  between '{}' and '{}'".format(f,l)
    cur.execute(qry)
    a=cur.fetchall()
    a=a[0][0]
    con.commit()
    qry="select COUNT(*) from ccms where age  between '{}' and '{}'".format(f,l)
    cur.execute(qry)
    m=cur.fetchall()
    m=m[0][0]
    con.commit()
    qry="select COUNT(*) from dcms where age  between '{}' and '{}'".format(f,l)
    cur.execute(qry)
    r=cur.fetchall()
    r=r[0][0]
    con.commit()
    qry="select COUNT(*) from ccms where age  between '{}' and '{}' and result = 'POSITIVE' and deathdt IS NULL".format(f,l)
    cur.execute(qry)
    b=cur.fetchall()
    b=b[0][0]
    con.commit()
    qry="select COUNT(*) from ccms where age  between '{}' and '{}' and status = 'DEAD'".format(f,l)
    cur.execute(qry)
    d=cur.fetchall()
    d=d[0][0]
    con.commit()
    qry="select count(*) from dpms where age  between '{}' and '{}' ".format(f,l)
    cur.execute(qry)
    k=cur.fetchall()
    k=k[0][0]
    con.commit()
    print("="*50)
    print("           Age Group(",f,"-",l,")   ",sep=" ")
    print("="*50)
    print("‣Total Tested",m+r)
    print("‣Total cases",a+k)
    print("‣Total  active cases present",b)
    print("‣Total recovered",a-(b+d))
    print("‣Total deaths",d+k)
    print("="*50)

# for displaing gender related information
def gender():
    print("="*50)
    print("\t","\t","Gender Wise Satistics")
    print("="*50)
    print("1. Male")
    print("2. Female")
    print("3. Transgenders")
    print("="*50)
    choice=int(input("Enter the option number to get the required service : "))
    if choice==1:
        ch="Male"
    elif choice==2:
        ch="Female"   
    elif choice==3:
        ch="Others"
    else:
        print('Option number',choice,' doesn’t exist')
    cur=con.cursor()
    qry="select COUNT(*) from tpms where GENDER = '{}'".format(ch)
    cur.execute(qry)
    a=cur.fetchall()
    a=a[0][0]
    con.commit()
    qry="select COUNT(*) from ccms where GENDER = '{}'".format(ch)
    cur.execute(qry)
    m=cur.fetchall()
    m=m[0][0]
    con.commit()
    qry="select COUNT(*) from dcms where GENDER = '{}'".format(ch)
    cur.execute(qry)
    r=cur.fetchall()
    r=r[0][0]
    con.commit()
    qry="select COUNT(*) from ccms where GENDER = '{}' AND RESULT='POSITIVE' and deathdt is null ".format(ch)
    cur.execute(qry)
    b=cur.fetchall()
    b=b[0][0]
    con.commit()
    qry="select COUNT(*) from ccms where GENDER = '{}' and status='DEAD'".format(ch)
    cur.execute(qry)
    d=cur.fetchall()
    d=d[0][0]
    con.commit()
    qry="select count(*) from dpms where GENDER = '{}'".format(ch)
    cur.execute(qry)
    k=cur.fetchall()
    k=k[0][0]
    con.commit()
    print("="*50)
    print("             GENDER (",ch,")   ")
    print("="*50)
    print("‣Total Tested",m+r)
    print("‣Total cases",a+k)
    print("‣Total  active cases present",b)
    print("‣Total recovered",a-(b+d))
    print("‣Total deaths",d+k)
    print("="*50)

#for displaying the details of a particular date
def time():
    print("="*50)
    print("\t","\t","Date Wise Statistics")
    print("="*50)
    try:
        date=input("Enter the Date(YYYY/MM/DD) : ")      
        cur=con.cursor()
        qry="select COUNT(*) from tpms where resultdt = '{}'".format(date)
        cur.execute(qry)
        a=cur.fetchall()
        a=a[0][0]
        con.commit()
        qry="select COUNT(*) from ccms where resultdt = '{}'".format(date)
        cur.execute(qry)
        b=cur.fetchall()
        b=b[0][0]
        con.commit()
        qry="select COUNT(*) from dcms where resultdt = '{}'".format(date)
        cur.execute(qry)
        m=cur.fetchall()
        m=m[0][0]
        con.commit()
        qry="select COUNT(*) from ccms where deathdt = '{}'".format(date)
        cur.execute(qry)
        k=cur.fetchall()
        k=k[0][0]
        con.commit()
        qry="select count(*) from dpms  where deathdt = '{}'".format(date)
        cur.execute(qry)
        j=cur.fetchall()
        j=j[0][0]
        con.commit()
        t=(a/(b+m))*100
        print("="*50)
        print("              Date (",date,")   ")
        print("="*50)
        print("‣Total  Tested",b+m)
        print("‣Total cases",a+j)
        print("‣Total  Death",k+j)
        print("‣Test Positivity Rate",round(t,2))
        print("="*50)
    except:
        print("No records exist for given date")
        print("="*50)

# for deleting the record using aadhar
def delete():
    try:
        cur=con.cursor()
        ad=input("Enter the Aadhaar ID of the person to be Deleted")
        qry="delete from ccms where aadhaar = '{}'".format(ad)
        cur.execute(qry)
        con.commit()
        qry="delete from tpms where aadhaar = '{}'".format(ad)
        cur.execute(qry)
        con.commit()
        qry="delete from dcms where aadhaar = '{}'".format(ad)
        cur.execute(qry)
        con.commit()
        qry="delete from dpms where aadhaar = '{}'".format(ad)
        cur.execute(qry)
        con.commit()
        print("Data Deleted Successfully")
    except:
        print("The given Aadhaar id does not exist ")

# for changing certain details of an induvijual
def change():
    try:
        cur=con.cursor()
        ad=input("Enter the Aadhaar ID of the person to be updated : ")
        print("1.To change Name")
        print("2.To change age")
        print("3.To change Gender")
        print("4.To change Local Body")
        print("5.To change District")
        print("6.To change result")
        print("7.To change resultdt")
        print("8.To change testdt")
        ch=int(input("Enter the option number to get the required service : "))
        if ch==1:
            s=input("Enter the Correct Name : ")
            qry="update ccms set name='{}'where aadhaar = '{}'".format(s,ad)
            cur.execute(qry)
            con.commit()
            qry="update tpms set name='{}'where aadhaar = '{}'".format(s,ad)
            cur.execute(qry)
            con.commit()
        elif ch==2:
            s=int(input("Enter the Correct Age : "))
            qry="update ccms set age='{}'where aadhaar = '{}'".format(s,ad)
            cur.execute(qry)
            con.commit()
            qry="update tpms set name='{}'where aadhaar = '{}'".format(s,ad)
            cur.execute(qry)
            con.commit()
        elif ch==3:
            s=input("Enter the Correct Gender : ")
            qry="update ccms set Gender='{}'where aadhaar = '{}'".format(s,ad)
            cur.execute(qry)
            con.commit()
            qry="update tpms set Gender='{}'where aadhaar = '{}'".format(s,ad)
            cur.execute(qry)
            con.commit()
        elif ch==4:
            s=input("Enter the Correct Local body : ")
            qry="update ccms set localbody='{}'where aadhaar = '{}'".format(s,ad)
            cur.execute(qry)
            con.commit()
            qry="update tpms set localbody='{}'where aadhaar = '{}'".format(s,ad)
            cur.execute(qry)
            con.commit()
        elif ch==5:
            s=input("Enter the Correct District : ")
            qry="update ccms set district='{}'where aadhaar = '{}'".format(s,ad)
            cur.execute(qry)
            con.commit()
            qry="update tpms set district='{}'where aadhaar = '{}'".format(s,ad)
            cur.execute(qry)
            con.commit()
        elif ch==6:
            s=input("Enter the Correct Result : ")
            qry="update ccms set result='{}'where aadhaar = '{}'".format(s,ad)
            cur.execute(qry)
            con.commit()
            qry="update tpms set result='{}'where aadhaar = '{}'".format(s,ad)
            cur.execute(qry)
            con.commit()
        elif ch==7:
            s=input("Enter the Correct Test date : ")
            qry="update ccms set testdt='{}'where aadhaar = '{}'".format(s,ad)
            cur.execute(qry)
            con.commit()
            qry="update tpms set testdt='{}'where aadhaar = '{}'".format(s,ad)
            cur.execute(qry)
            con.commit()
        elif ch==8:
            s=input("Enter the Correct Result Date : ")
            qry="update ccms set resultdt='{}'where aadhaar = '{}'".format(s,ad)
            cur.execute(qry)
            con.commit()
            qry="update tpms set resultdt='{}'where aadhaar = '{}'".format(s,ad)
            cur.execute(qry)
            con.commit()
        else:
            print('Option number',ch,' doesn’t exist')
        print("Data Updated Successfully")
    except:
        print("The given Aadhaar does not exist in the records")

# TPR Calculater
def tpr():
    print("="*40)
    print(" Test Positivity Rate calculator")
    print("="*40)
    t=int(input("enter  no of total  test : "))
    a=int(input("enter  no of positive cases : "))
    print("Test Positivity Ratio = ",round((a/t)*100,2))
    print("="*40)

# Weekly Infection Population Ratio (WIPR) Calculator
def wipr():
    print("="*40)
    print(" Weekly Infection Population Ratio (WIPR)")
    print("="*40)
    t=int(input("enter  no of total  cases in the week : "))
    a=int(input("enter  the population of the localbody : "))
    print("Weekly Infection Population Ratio  = ",round((t/a)*1000,2))
    print("="*40)    
bl="Nn"
while bl in "Nn":
    print(" ")
    print('+================================================+')
    print('|        Covid Case Management System            |')
    print('+================================================+')
    print("|1. Data Entry Portal                            |")
    print("|2. Covid Information Portal                     |")
    print("|3. Data Correction Portal                       |")
    print("|4. Instructions                                 |")
    print("|5. Positivity Rate calculator                   |")
    print('+------------------------------------------------+')
    choice=int(input("\n  Enter the option number to get the required service : "))
    if choice==1:
        bj="Nn"
        while bj in "Nn":
            print(" ")
            print('+================================================+')
            print("|              Data Entry Portal                 |")
            print('+================================================+')
            print("|1.To report new cases                           |")
            print("|2.To update present condition                   |")
            print("|3.To report dead cases                          |")
            print('+------------------------------------------------+')
            choi=int(input("\n  Enter the option number to get the required service : "))
            if choi==1:
                insert()
            elif choi==2:
                update()
            elif choi==3:
                dead()
            else:
                print('Option number',choi,' doesn’t exist')
            bj=input("Do you want to Exit Data Entry Portal,if yes 'Y' else 'N' - ")
    elif choice==2:
        br="Nn"
        while br in "Nn":
             print(" ")
             print('+================================================+')
             print('|        Covid Information Portal                |')
             print('+================================================+')
             print("|1. Search Personal Details                      |")
             print("|2. Details of  tested people                    |")
             print("|3. Active cases present                         |")
             print("|4. Details of dead covid cases                  |")
             print("|5. Statistics                                   |")
             print('+------------------------------------------------+')
             ch=int(input("\n Enter the option number to get the required service : "))
             if ch==1:
                 search()
             elif ch==2:
                 details()
             elif ch==3:
                 active()
             elif ch==4:
                 deathdetails()
             elif ch==5:
                 bc="Nn"
                 while bc in "Nn":
                     print(" ")
                     print('+================================================+')
                     print('|           Specific COVID Statistics            |')
                     print('+================================================+')
                     print("|1. District Based                               |")
                     print("|2. Local Body Based                             |")
                     print("|3. Age Group Based                              |")
                     print("|4. Gender Based                                 |")
                     print("|5. Date Based                                   |")
                     print('+------------------------------------------------+')
                     c=int(input("\n Enter the option number to get the required service : "))
                     if c==1:
                         district()
                     elif c==2:
                         localbody()
                     elif c==3:
                         age()
                     elif c==4:
                         gender()
                     elif c==5:
                         time()
                     else:
                         print('Option number',c,' doesn’t exist')
                     bc=input("Do You Want to Exit Covid Section Wise Satistics,if yes 'Y' else 'N' - ")
             else:
                 print('Option number',ch,' doesn’t exist') 
             br=input("Do You Want to Exit Covid Information Portal ,if yes 'Y' else 'N' - ")
    elif choice==3:
        bk="Nn"
        while bk in "Nn":
            print(" ")
            print('+================================================+')
            print('|             Rectification Portal               |')
            print('+================================================+')
            print("|1. Delete entries                               |")
            print("|2. change personal details                      |")
            print('+------------------------------------------------+')
            c=int(input("\n Enter the option number to get the required service : "))
            if c==1:
                delete()
            elif c==2:
                change()
            else:
                 print('Option number',c,' doesn’t exist')
            bk=input("Do You Want to Exit Covid Correction Portal ,if Yes 'Y' else 'N' - ")
    elif choice==4:
        print("="*50)
        print("\t","\t","INSTRUCTIONS","\t")
        print("="*50)
        print("1. Aadhaar Details cannot be changed once intialised")
        print("2. INPUT Date and other Details as Mentioned")
        print("3. ALL INPUTS HAVE TO MADE IN UPPERCASE")
        print("="*50)
    elif choice==5:
        print(" ")
        print('+================================================+')
        print('|         Positivity Rate calculator             |')
        print('+================================================+')
        print("|1. Test Positivity ratio(TPR)                   |")
        print("|2. Weekly Infection Population Ratio (WIPR)     |")
        print('+------------------------------------------------+')
        print(" ")
        ch=int(input("Enter the option number to get the required service : "))
        if ch==1:
            tpr()
        elif ch==2:
            wipr()
        else:
            print('Option number',ch,' doesn’t exist')     
    else:
        print('Option number',choice,' doesn’t exist')
    bl=input("Do You Want to Exit Covid Case Management System ,if Yes 'Y' else 'N' - ")
con.close()   
