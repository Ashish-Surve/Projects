import hashlib
import time

def md5(fpath): 
    hash_md5 = hashlib.md5()
    with open(fpath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    #print(hash_md5.hexdigest())        
    return hash_md5.hexdigest()
   

def time_deco(func):                            #calucate time taken can be used for any function and create sa log of the time taken in log.txt
    def updator(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()-start
        print("\n\nExecution time is : {}\n\n".format(end))
        fd=open("logs.txt",mode="a")
        fd.write("\nTime : {0}\tTime Taken : {1} seconds".format(time.asctime(time.localtime(time.time())),end))      #creating a lof file for checking times
        return result
    return updator    
