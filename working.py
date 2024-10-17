import re
import sys




def main():
    s = input("Hours: ").strip()
    print(convert(s))



def convert(s):
    time = {"1 AM": "01", "2 AM": "02",  "3 AM": "03", "4 AM": "04",
         "5 AM": "05", "6 AM": "06", "7 AM": "07", "8 AM": "08",
          "9 AM": "09", "10 AM": "10", "11 AM": "11", "12 AM": "00",
           "1 PM": "13", "2 PM": "14", "3 PM": "15", "4 PM": "16",
            "5 PM": "17", "6 PM": "18", "7 PM": "19", "8 PM": "20",
             "9 PM": "21", "10 PM": "22", "11 PM": "23", "12 PM": "12"}

    pattern = r"^((\d{1,2}):?(\d{2})? (AM|PM)) to ((\d{1,2}):?(\d{2})? (AM|PM))$"
    match = re.search(pattern, s)
    if match:
        start_minutes = ""
        end_minutes = ""

        start_hour = f"{match.group(2)} {match.group(4)}"
        end_hour = f"{match.group(6)} {match.group(8)}"

        if match.group(3):
            start_minutes = match.group(3)
            if int(match.group(3)) > 59:
                raise ValueError
        else:
            start_minutes = "00"
        if match.group(7):
            end_minutes = match.group(7)
            if int(match.group(7)) > 59:
                raise ValueError
        else:
            end_minutes = "00"

        return (f"{time[start_hour]}:{start_minutes} to {time[end_hour]}:{end_minutes}")

    else:
        raise ValueError



if __name__ == "__main__":
    main()
