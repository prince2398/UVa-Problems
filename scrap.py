import requests
from bs4 import BeautifulSoup
import os

url = "https://uva.onlinejudge.org/external/"

Errors = []

defaultCode = """#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    scanf("%d",&t);
    while(t--){
        //Write Code here
        
    }
    return 0;
}"""

def extractProblem(vol,n):
    path = str(vol)+'/'+str(vol*100 +n)
    res = requests.get(url+path+".pdf")

    if(res.status_code == 200):
        try:
            os.makedirs(path)
        except FileExistsError:
            pass

        with open(path+'/code.cpp',"w") as f:
            f.write(defaultCode)
        
        with open(path+'/'+str(vol*100 +n)+".pdf","wb") as f:
            f.write(res.content)
            print(path)
        
        
    else:
        Errors.append(int(str(vol)+str(n)))
    
for v in range(1,18):
    for i in range(0,100):
        extractProblem(v,i)