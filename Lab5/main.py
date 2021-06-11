import json


def run():
    user_config()


def user_config():
    web_server = str(input('enter web server: '))
    http_request = str(input('enter http request method: '))
    logging_level = str(input('enter logging level: '))
    log_lines = input('enter no. of log lines to be displayed: ')
    ip_address = input('enter ip address: ')

    lab_config = {
        "web_server": web_server,
        "http_request": http_request,
        "logging_level": logging_level,
        "log_lines": log_lines,
        "ip_address": ip_address
    }
    fileName = 'lab_config.json'

    with open(fileName, 'w') as f:
        json.dump(lab_config, f)

if __name__ == "__main__":
    run()

