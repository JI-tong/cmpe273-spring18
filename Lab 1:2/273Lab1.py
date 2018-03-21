from __future__ import print_function

import subprocess
import re
#import sys
#print(sys.version)

host = "ec2-reachability.amazonaws.com"

ip = {"us-east-1":"23.23.255.255", "us-west-1":"13.57.0.253","eu-west-1":"46.137.120.1","us-east-2":"13.58.0.253","us-west-2":"35.160.63.253",
"us-gov-west-1":"52.222.9.163","ca-central-1":"35.182.0.251",
      "sa-east-1":"54.94.191.252","eu-central-1":"18.194.0.252","eu-west-2":"35.176.0.252","eu-west-3":"52.47.32.127","ap-northeast-1":"13.112.63.251",
      "ap-northeast-2":"13.125.0.253","ap-southeast-1":"54.169.191.253",
      "ap-southeast-2":"54.66.191.252","ap-south-1":"35.154.63.252","cn-north-1":"54.222.240.4","cn-northwest-1":"52.83.214.0"}
result = {}
for i in list(ip.keys()):
    ping = subprocess.Popen(
        ["ping", "-c", "3", ip[i]],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, error = ping.communicate()
    out.decode()

    avg = out.split(b"/")
    #print(avg)
    result[float(avg[4])] = i

avgs = sorted(result.keys());

count = 1
for avg in avgs:

	print('{0} {1} [{2}] {3}ms'.format(str(count), result[avg], ip[result[avg]], str(avg)))

	count += 1

'''
1 us-west-1 [13.57.0.253] 5.143ms
2 us-west-2 [35.160.63.253] 25.948ms
3 us-gov-west-1 [52.222.9.163] 27.773ms
4 us-east-2 [13.58.0.253] 56.507ms
5 us-east-1 [23.23.255.255] 67.868ms
6 ca-central-1 [35.182.0.251] 79.523ms
7 ap-northeast-1 [13.112.63.251] 119.349ms
8 eu-west-2 [35.176.0.252] 142.085ms
9 eu-west-3 [52.47.32.127] 146.851ms
10 eu-west-1 [46.137.120.1] 151.845ms
11 ap-northeast-2 [13.125.0.253] 152.181ms
12 eu-central-1 [18.194.0.252] 158.005ms
13 cn-north-1 [54.222.240.4] 184.737ms
14 ap-southeast-2 [54.66.191.252] 189.646ms
15 ap-southeast-1 [54.169.191.253] 197.668ms
16 cn-northwest-1 [52.83.214.0] 198.73ms
17 sa-east-1 [54.94.191.252] 203.963ms
18 ap-south-1 [35.154.63.252] 350.357ms
'''
