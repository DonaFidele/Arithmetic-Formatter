#coding:utf-8
def arranger(operateur,operande1,operande2):
    dict={1:" ", 2:"  ", 3:"   ", 4:"    "}
    l="-"
    
    if len(operande1)>len(operande2):
        
        return f"  {operande1}\n{operateur} {dict[len(operande1)-len(operande2)]}{operande2}\n{l*(2+len(operande1))}"

    elif len(operande2)>len(operande1):
        
        return f"  {dict[len(operande2)-len(operande1)]}{operande1}\n{operateur} {operande2}\n{l*(2+len(operande2))}"
    else:
        
        return f"  {operande1}\n{operateur} {operande2}\n{l*(2+len(operande2))}"


def arithmetic_arranger(liste,true=None):
    dict={1:" ", 2:"  ", 3:"   ", 4:"    "}
    operations=[];som=[]

    if len(liste)>5:
        return "Error: Too many problems."
    
    for operation in liste:
        if '+' in operation:
            operande1=operation.split('+')[0].strip()
            operande2=operation.split('+')[1].strip()

            if len(operande1)>4 or len(operande2)>4:
                return "Error: Numbers cannot be more than four digits."
            elif not operande1.isdigit() or not operande2.isdigit():
                return "Error: Numbers must only contain digits."
            else:
                result=arranger("+",operande1,operande2)
                operations.append(result)
                som.append(int(operande1)+int(operande2))

        elif '-' in operation:
            operande1=operation.split('-')[0].strip()
            operande2=operation.split('-')[1].strip()

            if len(operande1)>4 or len(operande2)>4:
                return"Error: Numbers cannot be more than four digits."
            elif not operande1.isdigit() or not operande2.isdigit():
                return"Error: Numbers must only contain digits."
            else:
                result=arranger("-",operande1,operande2)
                operations.append(result)
                som.append(int(operande1)-int(operande2))
        else:
            return "Error: Operator must be '+' or '-'."

    liste1=[];liste2=[];liste3=[]
        
    for op in operations:
        line1=op.split('\n')[0]
        liste1.append(line1)
        #print(liste1)
      
        line2=op.split('\n')[1]
        liste2.append(line2)
        #print(liste2)
       
        line3=op.split('\n')[2]
        liste3.append(line3)
    
    fin=''
    #fin+='\n'
    for i in liste1:
        fin+=i
        if i==liste1[-1]:
          break
        else:
          fin+="    "
    fin+='\n'
    count=0
    for i in liste2:
        fin+=i
        if i==liste2[-1]:
          break
        else:
          fin+="    "
    fin+='\n'
    for i in liste3:
        fin+=i;count+=1
        if count==len(liste3):
          break
        else:
          fin+="    "
    


    if true==True:
        rsom=[]
        b=0
        #fin+='\n'
        for r in som:
          b+=1
          if b==1:
            fin+='\n'
            rsom.append(f"{dict[len(liste3[som.index(r)]) - len(str(r))]}{r}")
          else:
            rsom.append(f"{dict[len(liste3[som.index(r)]) - len(str(r))]}{r}")
        a=0
        for rs in rsom:
          a+=1
          fin+=rs
          if a==len(rsom):
            break
          else:
            fin+="    "
    return fin


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print('\n\n')
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))