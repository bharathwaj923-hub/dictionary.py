s={
    'name':'nikitha',
    'age':25,
    'city':'cleveland'
}
#method
s['job']='data engineering'
#method2
s.update(
    {
        'job':'data engineer'
    }
)
print(s)
print(s.get('sal'))
print(s.get('salary','not available'))
print(s.pop('city'))
print(s)
print('age' in s)
for keys in s.keys():
    print(keys)
for value in s.values():
    print(value)
for key,value in s.items():
    print(key,value)
s['age']=26
print(s['age'])
print(s)
#Count how many times each number appears:
s = [1, 2, 2, 3, 3, 3, 4, 4]
count={}
for i in s:
  if i in count:
      count[i]+=1
  else:
      count[i]=1
print(count)
student = {"name": "Nikitha", "age": 25, "city": "Cleveland"}
print(student['city'])
#Write a loop that prints only the keys whose values are numbers.
s={
    "name": "Nikitha",
    "age": 25,
    "salary": 50000
}
for key,value in s.items():
     if isinstance(value,int):
      print(key)
#Count the frequency of each word:
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
count={}
for i in words:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
#Find the largest value in this dictionary:
marks = {"Math": 85, "Python": 95, "SQL": 90}
largest=max(marks.values())
print(largest)
#key
print(max(marks,key=marks.get))
#Create a new dictionary containing only values greater than 80:
marks = {"Math": 75, "Python": 95, "SQL": 90, "Java": 70}

new_dict = {key: value for key, value in marks.items() if value > 80}

print(new_dict)
#
s = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(s['model'])
