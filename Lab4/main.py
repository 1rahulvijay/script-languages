import logging
import sys
import fileinput
import re




def run():
        logging.basicConfig(filename='log6.log',filemode='w', level=logging.DEBUG)
        logging.info("start")
        print("\n\n Task4 \n\n")
        lineDict = read_log()
        printDict(lineDict)
        print("\n\n Task 5 \n\n")
        myDictionary = ip_request(lineDict) #pass result of standard input read_log
        printDict(myDictionary)
        print("\n\n Task 6 \n\n")
        ip_find(myDictionary) #myDictionary holds number of requests per ip
        ip_find(myDictionary, False)
        print("\n\n Task 7 \n\n")
        print(longest_request(lineDict))
        print("\n\n Task 8 \n\n")
        print(non_existent(lineDict))
        logging.info("END")


def printDict(dict):
    count = 0
    for x in dict:
        print(str(x) + "    ::::::    " + str(dict[x]))
        count = count + 1
        if count > 5:
            return


def read_log():
    new_dictionary = {}
    splt_char = ''
    with open('accesslog4.txt', 'r') as f:
        for line in f:
            splitline = line.split()
            new_dictionary[splt_char.join(splitline[:5])] = splt_char.join(splitline[5:])
        return new_dictionary


def ip_request(dict):
    ip_dictionary = {}
    for x in dict:
        ip = x.split
        ipKey = 0
        ip_dictionary[ipKey] = ip_dictionary.get(ipKey, 0) + 1
    return ip_dictionary


def ip_find(d, most_active=True):
    ip_find_List = []
    if most_active == True:
        maxValue = max(d.values())
        for ip in d:
            if d[ip] == maxValue:
                ip_find_List.append((ip, d[ip]))
                print("Max Value")
                print(maxValue)

        else:
            minValue = min(d.values())
            for ip in d:
                if d[ip] == minValue:
                    ip_find_List.append((ip, d[ip]))
                    print("Min Value")
                    print(minValue)


def longest_request(dict):
    max = 0
    ip = {}
    longest_request_line = {}
    for x in dict:
        if len(x) > max:
            ip = x.split()
            max = len(x)
            longest_request_line = x
            longest_request_line = {
                "ip": ip,
                "length": max,
                "x": longest_request_line
            }
    return longest_request_line


def non_existent(dict):
    rSet = set()
    for x in dict:
        http_code = dict[x]
        http_code = http_code.split()
        http_error = 0
        request = x
        if http_error == "404":
            rSet.append(request)
    return rSet


if __name__ == "__main__":
    run()