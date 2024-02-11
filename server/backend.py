import requests
# from ProGPT import Generative, Conversation

URL = "https://zillow56.p.rapidapi.com/search"
URL2 = "https://zillow56.p.rapidapi.com/property"

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
    # change api key
	"X-RapidAPI-Key": "5eb3bd3ed8msh6d318f2c32b8c8cp17e3cfjsn8e855d87424a",
	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}

def get_search_response_from_zillow(
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
    sale_or_rent="forSale",
    url=URL,
    headers=HEADERS,
):
    
    price_min = int(price_min)
    price_max = int(price_max)
    beds_min = int(beds_min)
    beds_max = int(beds_max)
    baths_min = int(baths_min)
    baths_max = int(baths_max)
    square_feet_min = int(square_feet_min)
    square_feet_max = int(square_feet_max)
    
    
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
    "state=us": f"{sale_or_rent}",
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
    
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
        return None
    
    return response.json()

## PLEASE GET ZPID
## THIS IS HOW IT SHOULD BE
#  { zpid : ("image", "price, "address") }"}
    
def display_search_items(response):
    
    try:
        if response:
            
            n = int(response['totalResultCount'])
            
            display_array = []
            
            for item in response['results']:
                display_array.append({'zpid': item['zpid'], 'imgSrc': item['imgSrc'], 'price': item['price'], 'streetAddress': item['streetAddress']})        
            return display_array
        
        elif response == None:
            print("Error")
            return {"Error": "No response from Zillow"}
    
    except KeyError:
        print("Error")
        return {"Error": "No response from Zillow"}

def get_zpid_api_response(zpid, headers=HEADERS, url=URL2):
    querystring = {"zpid":f"{zpid}"}
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()
    
def display_zpid_info(response):
    # price
    # address
    # images array
    # home instights -> 0 -> insights -> phrases
    # nearbyhomes [extra]
    # rent or rent zestimate
    
    try:
        if response:
            
            photos = response["photos"]

            # Extract all the jpeg URLs with their respective widths
            jpeg_urls = [image["url"] for photo in photos for image in photo["mixedSources"]["jpeg"]]

            # Create a dictionary to store URLs based on their widths
            url_dict = {}
            for photo in photos:
                for image in photo["mixedSources"]["jpeg"]:
                    url_dict[image["width"]] = image["url"]

            # Get the maximum width of the jpeg images
            max_width = max(url_dict.keys())

            # Filter out only the JPEG URLs with the highest width
            imagesArray = [url_dict[width] for width in url_dict if width == max_width]
            
            try:         
                return {
                    "price": response['price'],
                    "address": response['abbreviatedAddress'],
                    "city": response['address']['city'],
                    "state": response['address']['state'],
                    "zip": response['address']['zipcode'],
                    
                    "bathrooms": response['bathrooms'],
                    "bedrooms": response['bedrooms'],
                    
                    "homeInsights": response['homeInsights'][0]['insights'][0]['phrases'],
                    "homeType": response['homeType'],
                    
                    "imagesArray": imagesArray,
                    "rentZestimate": response['rentZestimate'],
                    "mortgage15" : response['mortgageRates']['mortgage15YearFixedRate'],
                    "mortgage30" : response['mortgageRates']['mortgage30YearFixedRate'],
                }
                
            except (TypeError, ValueError, KeyError):
                return {
                    "price": response['price'],
                    "address": response['abbreviatedAddress'],
                    "city": response['address']['city'],
                    "state": response['address']['state'],
                    "zip": response['address']['zipcode'],
                    
                    "bathrooms": response['bathrooms'],
                    "bedrooms": response['bedrooms'],
                    
                    "homeInsights": response['homeInsights'][0]['insights'][0]['phrases'],
                    "homeType": response['homeType'],
                    
                    "imagesArray": imagesArray,
                    "rentZestimate": response['rentZestimate'],
                }
            
        
        elif response == None:
            print("Error")
            return {"Error": "No response from Zillow"}
    
    except KeyError:
        print("Error")
        return {"Error": "No response from Zillow"}
    
  
if __name__ == "__main__":
    
    
    # response_api = get_search_response_from_zillow(
    #     location="08852",
    #     price_min=100000,
    #     price_max='500000',
    #     beds_min=1,
    #     beds_max=3,
    #     baths_min=1,
    #     baths_max=3,
    #     square_feet_min=1000,
    #     square_feet_max=2000,
    #     sale_or_rent="forRent",
    #     isApartment=True,
    #     isCondo=True,
    #     isTownhouse=True,
    # )
    
    # display_array = display_search_items(response_api)

    # for item in display_array:
    #     print(f"ZPID: {item['zpid']} \n Image: {item['imgSrc']} \n Price: {item['price']} \n Address: {item['streetAddress']}")
    #     print("\n")   
    
    rep = get_zpid_api_response(2062003050)
    print(display_zpid_info(rep))
        
        
