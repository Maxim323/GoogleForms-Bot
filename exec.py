import re
import time
start_time = time.time()

Demo = 'https://docs.google.com/forms/d/e/1FAIpQLSfVAfLRrBPkhP55_1jrP9IrPys99BjayAzQ_G_EM2bJ0iNd_w/viewform?usp=pp_url&entry.2098263493=2&entry.1497167764=2&entry.1495890103=2&entry.1012177044=2'



start = Demo[:116]
start = start.replace('viewform','formResponse')

result = re.search('entry(.*)&',Demo)
result = result.group(1)
result = result.replace('=2','=%s')
final = start + result


print(start)
print(result)
print(final)
print("Time while running: %s seconds." % (time.time() - start_time))
