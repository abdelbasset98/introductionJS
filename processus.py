import os
from multiprocessing import Process,current_process
list_p=[]
list_imp=[]
def task(n):
  global list_p
  global list_imp
  if current_process().name=='P-1':
   for i in range(n):
    if i%2==0:
         list_p.append(i)
    else:
         for i in range(n):
            if i%2!=0:
                list_imp.append(i)
  """   if current_process().name=='P-1':
        print(f'hello {os.getpid()}')
    else: 
        print(f'world {os.getpid()}') """
    #print(f' child process id : pid={os.getpid()},process name={current_process().name}')

if __name__ == '__main__':
    process_1=Process(target=task,args=[10],name='P-1')
    process_2=Process(target=task,args=[20],name='P-2')
    process_1.start()
    #process_1.join()
    process_2.start()
    process_2.join()
    process_1.join()
    print(list_p)
    print(list_imp)
