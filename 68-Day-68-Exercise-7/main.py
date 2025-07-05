import os
print(os.getcwd())
os.chdir("/Users/Ankit/Desktop/vscode/git pulled/100 days python by harry/python-100-days-of-code-youtube/68-Day-68-Exercise-7/clutter")
print(os.getcwd())

files=os.listdir()
print(files)
dict={}
for file in files:
    ind=file.rindex(".")
    # print(ind)
    fname=file[:ind]
    ext=file[ind:]
    # print(ext)
    # if(dict[ext].exists):
    #     pass
    if ext not in dict:
        dict[ext]=1
        os.mkdir(ext[1:])
    else:
        dict[ext]+=1
    
    os.rename(f"{fname}{ext}",f"{ext[1:]}/{dict[ext]}{ext}")

for key,value in dict.items():
    print(key,value)