##
# strings
print("Hello, World!")
# I'm Nhan
print("I\"m Nhan")

print("a\tb\nc")
'''
a   b
c

hi
hello
bye
'''
print("""hi
hello
bye""")

s = input("write smth: ")
print(s.lower())

##
age = 22
print(age)
print(100)

jfk = 1963
print(jfk)

a = b = 4
print(a + b)

##
sgd = int(input("Amount: "))
print(sgd * 20355)

##
print('a' + 'b' ' cd')  # ab cd

##
name = "John"
age = 24

print(f"{name} is {age * 12} months old!")  # John is 288 months old!

##
a = input("write: ")
# print(a)

##
user_name = " ROLF SMITH  "
user_name = user_name.strip()  # "ROLF SMITH"
user_name = user_name.title()  # "Rolf Smith"
print(user_name)

##
greeting = "Hello, World"
print(greeting + '!')
print(f"{greeting}!")
print("{}!".format(greeting))
##
name = input("ur name: ").strip().title()
print("Hello, {}".format(name))

##
age = int(input("ur age: "))
print("I am " + str(age))

##
title = "joker"
director = "toDd phillips"
release_year = 2019

print(f"{title.title()} ({release_year}), directed by {director.title()}")

##
p = int(input())
q = int(input())
r = int(input())
s = int(input())
u = int(input())
v = int(input())
a = 0
b = 0
c = 0
if p==q:
    a+=1
    b+=1
if p<q:
    b+=3
if p>q:
    a+=3
if r==s:
    a+=1
    c+=1
if r<s:
    c+=3
if r>s:
    a+=3
if u==v:
    c+=1
    b+=1
if u<v:
    c+=3
if u>v:
    b+=3
print(a)
print(b)
print(c)
##
n = int(input())
if n%10<=5:
    print(int(n/10)*10)
else:
    print(round(n/10)*10)
##
k = int(input())
kc = 2024-k
if kc%2==0 and k<2024:
    print(kc//2)
else:
    print(-1)


##
a = int(input())
b = 1
if a>300:
    print((a-300)*1500 + (300*1200))
else:
   print(a * 1200)
##
n = int(input())
if n%500>=3:
    print(500*50 + 500*40 + 500*30 + (1500-n)*25)
if n%500==2:
    print(500*50 + 500*40 + (1000-n)*30)
if n%500==1:
    print(500 * 50 + 500 * 40 + (1000 - n) * 30)


##

