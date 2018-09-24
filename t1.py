uid ="vikzas"
session = "1"
open('t2.py', 'w').close()
fruits=["global userid\n","userid = '"+uid+"'\n","global session\n","session = '"+session+"'\n"]
new_file=open("t2.py",mode="a+",encoding="utf-8")
new_file.writelines(fruits)
for line in new_file:
    print(line)

new_file.close()