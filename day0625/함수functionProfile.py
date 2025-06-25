
def profile1(name, age, *language): # 가변 인자
    print("이름 : {0}\t나이 : {1} ".format(name, age), end=" ") 
    for lang in language:
        print(lang, end=" ")
    print()
  

profile1("유재석", 30, "LLM", "RAG", "bigData", "python", "MLAI", "opencv2")    
profile1("조세호", 35, "리액트", "노드node")
print('- ' * 60)
print()



def profile2(name, age, *skills):
    profile_info = {
        "name": name,
        "age": age,
        "skills": list(skills)
    }
    return profile_info


user1 = profile2("유미래", 30, "django", "react", "bigData", "python", "pandas", "numpy")
user2 = profile2("유미지", 35, "java", "spring")

print("User 1:", user1)
print("User 2:", user2)
print('- ' * 60)
print()


def profile3(x,y,*z):
  name,age = x,y
  lan = z
  print(f'이름 : {name}\t나이 : {age}\n언어 : {lan}\n')


profile3("이패스", 30, "django", "react", "bigData", "python", "pandas", "numpy")
profile3("김합격", 35, "java", "spring")