import re
def main():

    ip = input('IPv4 Address: ').strip()

    result = validate(ip)
    if result:
        print('True')

    else:
        print('False')

def validate(ip):
    if re.search(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip):
        number = ip.split('.')
        ip_address = 0
        for n in number:
            if int(n) <= 255:
                ip_address += 1

        if ip_address == 4:
            return True
        else:
            return False
    else:
        return False





if __name__ == '__main__':
    main()
