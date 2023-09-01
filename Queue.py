f=0
r=0
q=[]

def isEmpty(q):
    if(q==[]):
        return True
    else:
        return False


def nq(q,ele):
    global r
    q.append(ele)

    if(len(q)==1):
     f=r=0
    else:
     r=len(q)-1


def dq(q):
  global r
  if(isEmpty(q)):
    print('underflow')
  else:
    f=q[r]
    q.pop(0)
    r=r-1
    return(f)
    

   

def disq(q):

  for i in range(f,r+1):
     print(q[i])


def Execute(choice):

    global q
    if choice == '1':
        ele = input("ENTER ELEMENT TO ENQUEUE: ")
        nq(q, ele)
    elif choice == '2':
        ele = dq(q)
        if ele is not None:
            print(f"{ele} is deleted from QUEUE")
    elif choice == '3':
        disq(q)
    else:
        print("Invalid choice")

if __name__=='__main__':

 while(True):
   choice=input("1.ENQUEUE \n2,DEQUEUE \n3.DISPLAY ")
   Execute(choice)
