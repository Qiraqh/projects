import requests
import sys

def main():
    try:

        number_of_bitcoin = float(sys.argv[1])
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        btc = r.json()
        price = float(btc['bpi']['USD']['rate_float'])
        amount = number_of_bitcoin * price
        print(f'${amount:,.4f}')
    except requests.RequestException:
        sys.exit("Request Error")

    except IndexError:
        sys.exit("Missing command-line argument")

    except ValueError:
        sys.exit("Command-line argument is not a number")



if __name__ == "__main__":
    main()

