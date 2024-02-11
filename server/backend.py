import requests

URL = "https://zillow56.p.rapidapi.com/search"

querystring = {
    "location":"houston, tx",
    # defualt values included in every request
    "output":"json",
    "sortSelection":"featured",
    "isForSaleByOwner":"true",
    "isForSaleByAgent":"true",
    "isComingSoon":"false",
    "onlyWithPhotos":"true", 
    }

HEADERS = {
	"X-RapidAPI-Key": "8960a9414bmsh79b0e7d134ed3eap198937jsn3a471298130f",
	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}

def get_api_response_from_zillow(
    location,
    price_min,
    price_max,
    beds_min,
    beds_max,
    baths_min,
    baths_max,
    square_feet_min,
    square_feet_max,
    isApartment,
    isCondo,
    isTownhouse,
    url=URL,
    headers=HEADERS,
    
    
):
    
    if isApartment == True:
        isApartment = "true"
    else:
        isApartment = "false"
    
    if isCondo == True:
        isCondo = "true"
    else:
        isCondo = "false"
        
    if isTownhouse == True:
        isTownhouse = "true"
    else:
        isTownhouse = "false"
    
    querystring = {
    "location": f"{location}",
    # defualt values included in every request
    "output":"json",
    "sortSelection":"featured",
    "isForSaleByOwner":"true",
    "isForSaleByAgent":"true",
    "isComingSoon":"false",
    "onlyWithPhotos":"true",
    # undefault values
    "price_min": f"{price_min}",
    "price_max": f"{price_max}",
    "beds_min": f"{beds_min}",
    "beds_max": f"{beds_max}",
    "baths_min": f"{baths_min}",
    "baths_max": f"{baths_max}",
    "square_feet_min": f"{square_feet_min}",
    "square_feet_max": f"{square_feet_max}",
    "isApartment": f"{isApartment}",
    "isCondo": f"{isCondo}",
    "isTownhouse": f"{isTownhouse}",
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

    


if __name__ == "__main__":
    
    print(get_api_response_from_zillow(
        location="08852",
        price_min=100000,
        price_max=500000,
        beds_min=1,
        beds_max=3,
        baths_min=1,
        baths_max=3,
        square_feet_min=1000,
        square_feet_max=2000,
        isApartment=True,
        isCondo=True,
        isTownhouse=True,
    ))
    
