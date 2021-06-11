import json
import logging


def run():
    data_config()
    lineDict = read_log()
    print(lineDict)
    mydict = print_all_request(lineDict)
    print(mydict)
    print_requests_according_to_config(lineDict)
    print_requests_for_given_browser(lineDict)




# TASK 2
def data_config():
    fname = 'lab_config.json'
    config = {}
    logs = {}

    try:
        f = open(fname)
        config = json.load(f)
    except FileNotFoundError:
        print("file does not exist")
    except ValueError:
        print("json file is not correc")
    try:
        logs = config.get("web_server_name")
    except FileNotFoundError:
        print("Log file not found")

# task 3
def set_logging_level(level):
    if level == "DEBUG":
        logging.basicConfig(level=logging.DEBUG)
    elif level == "INFO":
        logging.basicConfig(level=logging.INFO)
    elif level == "ERROR":
        logging.basicConfig(level=logging.ERROR)
    elif level == "WARNING":
        logging.basicConfig(level=logging.WARNING)

def read_log():
    new_dictionary = {}
    splt_char = ''
    with open('accesslog4', 'r') as f:
        for line in f:
            splitline = line.split()
            new_dictionary[splt_char.join(splitline[:5])] = splt_char.join(splitline[5:])
        return new_dictionary


# task 4
def print_all_request(dict):
    dictionary = {}
    resource_dict = {}
    for x in dict:
        line =  x.split
        method = 0
        resource = 0
        dictionary[method] = dictionary.get(method, 0) + 1
        resource_dict[resource] = resource_dict.get(resource, 0) + 1

    if str(resource).find("index.html") >=0:
        print(method, resource)

# task 5

def print_requests_according_to_config(d):
    http_method = []
    counter = 0
    for x in d.values():
        http = x[4].split(" ")[0]
        if http == http_method:
            print(x)
            counter += 1

def print_requests_for_given_browser(dict):
    invalid_logs = 0
    for x in dict:
        user_info = x[8]
        if str(user_info).find("my_own") >= 0:
            print(x)

    assert invalid_logs == 0, "Invalid logs found in log file!"
    msg = "method: print_request invalid_logs readed: {}"
    logging.debug(msg.format(invalid_logs))

if __name__ == "__main__":
    run()