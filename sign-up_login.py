import json

name=input("Please Enter Your Name... :)")
print("Hello",name)

user=input("Enter what you want :)\n1.signup\n2.login\n")

if user=="1" or user=="signup":
    userName=input("Enter your userName--")
    password1=input("Enter password--")
    password2=input("Enter the confirm password--")
    Dob=input("enter your date of birth--")
    gender=input("enter male / female--")
    hobby=input("enter your hobby--")

    
    dic={"userName":userName,"password":password1,"profile":{"DOB":Dob,"Gender":gender,"Hobby":hobby}}

    if len(password1)>=8 and "@" in password1 or "#" in password1:

            if password1==password2:
            
                with open('user-details.json','r') as f:
                    userData=json.load(f)
                    for i in userData['user']:
                        if i['userName']==userName and i['password']==password1:
                            print("User already Exist :)")
                            break
                    else:
                
                        with open('user-details.json') as file: 
                            data = json.load(file) 

                            data3 = data["user"] 

                            data3.append(dic)

                
                        with open("user-details.json","w") as data1:
                            json.dump(data, data1,indent=4)

                        print("congurlation",userName,"you account succesfully created....")
        
            else:
                print("your password not same please enter same password--")
    else:
        print("in your password no special character at least put 1 special character ")


else:
    if user=="2" or user=="login": 

        print('Hey:',name, 'Welcome To Login Page :)')
        userName=input("enter the userName:) ")
        loginPassword=input('enter the password:)')
     
        with open('user-details.json','r') as f:
            userData=json.load(f)
            for i in userData['user']:
                if i['userName']==userName and i['password']==loginPassword:
                    print("Login Successfully :)")
                    break
                    
            else:
                print("\npassword/userName is wrong")
                
    else:
        print('Please Enter The Correct Input')
        
