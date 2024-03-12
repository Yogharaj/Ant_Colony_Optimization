import random
import requests
from flask import Flask,request,render_template
app = Flask(__name__)

server1="172.17.0.2:5000"
server2="172.17.0.3:5001"
server3="172.17.0.4:5002"
c1=0;c2=0;c3=0;
p=100000
m1={0:server1,1:server2,2:server3}        

def calculate_probability(c1,o1):
    ans=(p-c1)/o1
    return ans

@app.route('/', methods=['POST'])
def handle_client():
    n = int(request.form.get('n'))
    l1=list()
    global c1
    global c2
    global c3
    o1=(p-c1)+(p-c2)+(p-c3)
    p1=calculate_probability(c1,o1)
    p2=calculate_probability(c2,o1)
    p3=calculate_probability(c3,o1)
    v=max(p1,p2,p3)
    if p1==v: l1.append(0)
    if p2==v: l1.append(1)
    if p3==v: l1.append(2)
    n1=len(l1)-1
    r=random.randint(0,n1)
    data = {'n': n}
    ser=m1[l1[r]]
    r=l1[r]
    if r==0: c1+=1
    if r==1: c2+=1
    if r==2: c3+=1
    r+=1
    url = 'http://'+ser
    response=requests.post(url,data).text
    s="Server "+str(r)+":"
    ans=s
    ans+=("2 power "+str(n)+" is "+response)
    return ans

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5003)

    


