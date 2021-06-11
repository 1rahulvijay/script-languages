import logging
import re
import sys
import ipaddress


# Task 2
def readConfig():
    try:

        fname = "lab6.config"
        f = open(fname)
        read_lines = f.read()

        f = re.compile("(\\[LogFile]\\nname=)(.*)")
        filename = (f.findall(read_lines))[0][1]

        a = re.compile(r'(\[Config]\ndebug=)(.*)')
        config = (a.findall(read_lines))[0][1]
        getLogLevel(config)

        b = re.compile(
            r'(\[Display]\n)(lines=)(.*)(\nseparator=)(.*)(\nfilter=)(.*)')
        display = (b.findall(read_lines))[0]

        lines = display[2]
        separator = display[4]
        filter = display[6]

        if (lines == ''):
            lines = '10'
        if (separator == ''):
            separator = '|'
        if (filter == ''):
            filter = 'GET'

        displaySettings = {
            "lines": lines,
            "separator": separator,
            "filter": filter
        }

    except FileNotFoundError:
        print("file with this name doesn't exist")
        logging.error("file with this name doesn't exist")
        sys.exit()

    print(displaySettings)
    return (filename, displaySettings)


def getLogLevel(level):
    if level == "DEBUG":
        logging.basicConfig(level=logging.DEBUG)
    elif level == "INFO":
        logging.basicConfig(level=logging.INFO)
    elif level == "ERROR":
        logging.basicConfig(level=logging.ERROR)
    elif level == "WARNING":
        logging.basicConfig(level=logging.WARNING)


# Task 3
def readlogfile(log_file):
    linesArray = []
    try:
        f = open(log_file + ".txt")
        for line in f:
            linesArray.append(line)
    except OSError:
        logging.error("File read error!")
        sys.exit()
    return linesArray


# Task 4
def analyzelogfile(lines):
    result = []

    for line in lines:

        i = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
        ip_add = i.search(line).group()

        t = re.compile(r'\[(.*?)]')
        tstamp = t.search(line).group()

        h = r'\"(.*?)\"'
        http_header = (re.findall(h, line))[0]

        c = r'("\s)(\d{3})'

        http_status_code = (re.findall(c, line))[0][1]

        s = r'(\d+)(\s")'
        size = (re.findall(s, line))
        if len(size) == 1:
            size = size[0][0]
        else:
            size = 0

        result.append((ip_add, tstamp, http_header, http_status_code, size))
    return result


# TASK 5

def getRequests(loglinearray, interval):

    ip = "144.76.38.40"
    # 245784 % 16 + 8 = 16
    netmask = "255.255.0.0"


    net = ipaddress.ip_network(ip+'/'+netmask, strict=False)
    subnet = net.network_address

    counter = 1
    for line in loglinearray:
        if belongsToSubnet(line[0], netmask, subnet):
            if counter > interval and interval > 0:
                input("Press enter to continue")
                counter = 1
            print(line)
            counter += 1


def belongsToSubnet(ip, mask, subnet):
    net = ipaddress.ip_network(ip+'/'+mask, strict=False)
    if net.network_address == subnet:
        return True
    else:
        return False


# TASK 6
def sumofBytes(fileconfig):
    total = 0
    filter = fileconfig.get("filter")
    sep = fileconfig.get("separater")

    with open('access log-20201025.txt', 'r') as f:
        logs = f.readlines()

        for log in logs:
            Type = re.findall(r"\"[A-Z]{3,4}", log.split("\"-\"")[0])
            if len(Type) > 0:
                Type2 = Type[0][1:]

            stat_size = re.findall(r"\d\d\d", log.split("\"-\"")[0])
            size = stat_size[1]

            if Type2 == filter:
                total += int(size)

    print(filter, sep, total)


def run():
    fileconfig = readConfig()

    requestLines = readlogfile(fileconfig[0])
    loglinearray = analyzelogfile(requestLines)

    getRequests(loglinearray, int(fileconfig[1].get("lines")))
    sumofBytes(fileconfig[1])


if __name__ == "__main__":
    run()