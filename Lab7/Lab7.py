import datetime
import ipaddress
import re


def getmonth(month):
    if month == "Jan":
        return 1
    elif month == "Feb":
        return 2
    elif month == "Mar":
        return 3
    elif month == "Apr":
        return 4
    elif month == "May":
        return 5
    elif month == "Jun":
        return 6
    elif month == "Jul":
        return 7
    elif month == "Aug":
        return 8
    elif month == "Sep":
        return 9
    elif month == "Oct":
        return 10
    elif month == "Nov":
        return 11
    elif month == "Dec":
        return 12
    else:
        return 1


def returntimebbject(timestamp):
    timesplit = timestamp[1:-1].split(':')
    datesplit = timesplit[0].split('/')

    day = int(datesplit[0])
    month = int(getmonth(datesplit[1]))
    year = int(datesplit[2])

    hour = int(timesplit[1])
    minute = int(timesplit[2])
    second = int(timesplit[3][0:2])

    x = datetime.datetime(year, month, day, hour, minute, second)
    return x


# task 5
class HttpRequest:
    def __init__(self, request):
        request = request.split(" ")
        self.method = request[0]
        self.requested_resource = request[1]
        self.protocol = request[2]

    def req_string(self):
        return " \nmethod:" + self.method + " \nresource:" + self.requested_resource + " \n protocol:" + self.protocol


# task 6
class LogLine:
    def __init__(self, log_tuple):
        if not checklogline(log_tuple):
            raise MalformedHttpReq("Malformed HTTP request! ")
        self.ip = ipaddress.IPv4Address(log_tuple[0])
        self.timestamp = returntimebbject(log_tuple[1])
        self.http_request = HttpRequest(log_tuple[2])
        self.status_code = int(log_tuple[3])
        self.size = int(log_tuple[4])

    def to_string(self):
        return "IP:" + str(self.ip) + " \tTIMESTAMP:" + str(self.timestamp) + " \tSTATUS_CODE:" + str(
            self.status_code) + " \tSIZE:" + str(self.size) + self.http_request.req_string()


# task7
def logfile(line):
    i = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
    ip = i.search(line).group()

    t = re.compile(r'\[(.*?)]')
    timestamp = t.search(line).group()

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

    result = (ip, timestamp, http_header, http_status_code, size)

    return LogLine(result)


def checklogline(line):
    if len(line) != 5:
        return False
    elif line[2].split(" ")[0] not in ['GET', 'POST', 'CONNECT', 'PUT', 'HEAD', 'TRACE', 'PATCH', 'OPTIONS', 'DELETE']:
        return False
    else:
        return True


def getrequests(logarray, time_interval_first, time_interval_second):
    if time_interval_first > time_interval_second:
        print("second interval is smaller so cannot process ahead!")
        return
    for log in logarray:
        timestamp = log.timestamp

        if time_interval_first < timestamp < time_interval_second:
            print(log.to_string())


# task 9
class MalformedHttpReq(Exception):
    def __init__(self, message):
        super().__init__(message)


def logfilewithexceptions(f):
    no_of_exception = 0
    logarray = []
    for line in f:
        try:
            logline = logfile(line)
            logarray.append(logline)
        except MalformedHttpReq:
            no_of_exception += 1
    print("EXCEPTIONS FOUND: ", no_of_exception)
    return logarray


def read_log(filename):
    f = open(filename)
    logarray = logfilewithexceptions(f)

    return logarray


def run():
    logarray = read_log('access log-20201025.txt')
    time1 = returntimebbject('[18/Oct/2020:12:00:00 +0200]')
    time2 = returntimebbject('[20/Oct/2020:12:00:00 +0200]')
    getrequests(logarray, time1, time2)


if __name__ == "__main__":
    run()
