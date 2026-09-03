#1
try :
    with open("data/exercice.txt","r") as file:
        content = file.readlines()
    
    res = {}
    
    # print(content)
    
    for line in content:
        set_line = line.split()
        # print(set_line)
        if set_line[0] in res:
            res[set_line[0]].append(" ".join(set_line[1:]))
        else :
            res[set_line[0]] = [" ".join(set_line[1:])]
         
    # for i ,v in res.items():
    #     print(i , ":" , v)
    
except Exception as e:
    print(e)
    
    
#2

try :
    
    with open("data/resume_logs.txt","w") as file:
        text = ""
        for c , v in res.items() :
            text += f"{c} : {len(v)} \n"
            
            
        file.write(text)
        
        
    
        
except Exception as e:
    print(e)