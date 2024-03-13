import random
import requests
from flask import Flask,request,render_template
from collections import defaultdict

app = Flask(__name__)

server1="172.17.0.2:5000"
server2="172.17.0.3:5001"
server3="172.17.0.4:5002"
m2=defaultdict(int)
p=100000
m1={0:server1,1:server2,2:server3}    
servers=list()
for i in range(3):
    d="http://"+m1[i]
    servers.append(d)

def calculate_probability(c1,o1):
    ans=(p-c1)/o1
    return ans

def check_server(url):
    try:
        response = requests.post(url, data={'n': 2})
        if response.status_code == 200:
            return True
    except Exception as e:
        print(f"Error: {e}")
    return False

@app.route('/', methods=['POST'])
def handle_client():
    n = int(request.form.get('n'))
    global m2
    l1=list()
    l2=list()
    i=0
    for url in servers:     
        if check_server(url):
            l1.append(i)
        i+=1
    #print(len(l1))
    mi=0
    tot=0
    for i in l1:
        tot+=(p-m2[i])
    for i in l1:
        d1=calculate_probability(m2[i],tot)
        d2=mi
        mi=max(d2,d1)
    #print(mi)
    for i in l1:
        if calculate_probability(m2[i],tot)==mi:
            l2.append(i)
    n1=len(l2)-1
    r=random.randint(0,n1)
    data = {'n': n}
    ser=m1[l2[r]]
    r=l2[r]
    m2[r]+=1
    r+=1
    url = 'http://'+ser
    response=requests.post(url,data).text
    s="Server "+str(r)+":"
    ans=s
    ans+=("2 power "+str(n)+" is "+response)
    return ans

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5003)

    


