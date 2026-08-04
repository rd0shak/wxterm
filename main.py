import json
from urllib.request import urlopen

def query_airport(id):
    # https://aviationweather.gov/api/data/metar?ids=KJFK&format=json
    # I need to parse JSON for this, airport queries seems easy enough
    print("hello")

def main():
    """ 
    Default output should be simple, the number and degree for temp, some kind
    of symbols for the conditions. Can use shorthand or emoji, and need to
    figure out how to pull the data in the first place. I'll also probably need
    some sort of help or usage information, for features and options!
    """
    # Test output
    print("72°")
    print("72°☀️")
    print("☀️")


if __name__ == "__main__":
    main()
