import sys

year = int(input("Enter the year of the Ferrari 250 GTO you want to find the value for"))
if year < 1962:
    print("Unfortunately no Ferrari's existed during this time period")
    sys.exit()
elif year <= 1964:
    print("The estimated value of the vehicle was $18,500")
    sys.exit()
elif year <= 1968:
    print("The estimated value of the vehicle was $6,000")
    sys.exit()
elif year <= 1971:
    print("The estimated value of the vehicle was $12,000")
    sys.exit()
elif year <= 1980:
    print("The estimated value of the vehicle was $200,000")
    sys.exit()
elif year <= 1985:
    print("The estimated value of the vehicle was $650,000")
    sys.exit()
elif year <= 2012:
    print("The estimated value of the vehicle was $35,000,000")
    sys.exit()
elif year <= 2014:
    print("The estimated value of the vehicle was $52,000,000")
    sys.exit()
else:
    print("The price data is not unvailable. Thank you")