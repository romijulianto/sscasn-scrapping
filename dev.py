import requests
import pandas as pd
import string

access_token = 'Bearer eyJ0eXAiOiJKV1QiLCJub25jZSI6Im1obF9kd3RjdWxFLTQydUhvMFNqREh6YkZ6bHYzS19iaHlDSW1VUHhBeTQiLCJhbGciOiJSUzI1NiIsIng1dCI6Ikg5bmo1QU9Tc3dNcGhnMVNGeDdqYVYtbEI5dyIsImtpZCI6Ikg5bmo1QU9Tc3dNcGhnMVNGeDdqYVYtbEI5dyJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8xNGJiMmI2Ny00Y2QzLTQyY2YtYTVjMy1hNjNhYWY1MjQ1YWMvIiwiaWF0IjoxNzI1NTI4NTQ2LCJuYmYiOjE3MjU1Mjg1NDYsImV4cCI6MTcyNTUzMjgxOSwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhYQUFBQVR1aGVqdmRmVCtwZzhKVFByNmZSVDBzL3BRL3Nsd1JyNVhqM25DZGRGd3NlS3FWeUh6RzZERkpUbG5XTFFQZksiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6Ik1pY3Jvc29mdCBGbG93IFBvcnRhbCIsImFwcGlkIjoiNjIwNGMxZDEtNDcxMi00YzQ2LWE3ZDktM2VkNjNkOTkyNjgyIiwiYXBwaWRhY3IiOiIwIiwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiMTE0LjQuMjEyLjIzMiIsIm5hbWUiOiJDb21tYW5kIENlbnRlciIsIm9pZCI6ImMwM2EzMGU1LWRkYmEtNGU3ZC1iZGUyLTk3NmI5MGFlMzQyYSIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0yMTE0OTExMjkzLTM0MTAyNDM2NzctMTA4Mjg1NTI0Ny00MTI4OTQiLCJwbGF0ZiI6IjUiLCJwdWlkIjoiMTAwMzIwMDEzQzMwMDQ5OSIsInJoIjoiMC5BVllBWnl1N0ZOTk16MEtsdzZZNnIxSkZyQU1BQUFBQUFBQUF3QUFBQUFBQUFBQ2VBTk0uIiwic2NwIjoiZW1haWwgRmlsZXMuUmVhZCBGaWxlcy5SZWFkLkFsbCBvcGVuaWQgUGVvcGxlLlJlYWQgcHJvZmlsZSBTaXRlcy5SZWFkLkFsbCBVc2VyLlJlYWQgVXNlci5SZWFkLkFsbCIsInN1YiI6Il9YbkZELXBsdkVNa2lRU25NZ1NKSG91bWdfZHNDcVZ1NVN1SFdYbnRZVEEiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiQVMiLCJ0aWQiOiIxNGJiMmI2Ny00Y2QzLTQyY2YtYTVjMy1hNjNhYWY1MjQ1YWMiLCJ1bmlxdWVfbmFtZSI6ImNvbW1hbmQuY2VudGVyQHBlcnRhbWluYS5jb20iLCJ1cG4iOiJjb21tYW5kLmNlbnRlckBwZXJ0YW1pbmEuY29tIiwidXRpIjoiWlhacXlRNzJ4RXV5bjk3ZExkVVdBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19pZHJlbCI6IjEgNiIsInhtc19zdCI6eyJzdWIiOiJpUmJzTXBNZ3dyTlZfSUVNTzBfZnFhQkllZGJvcEV1LXdyRWxUNFR1Rk9RIn0sInhtc190Y2R0IjoxNDk5OTE1ODIyfQ.fu82AfMZk9c8Uuf__zDm2n03AbfBsP05mZOoJ9XbCcGfKhBGCx7YhJEsIsi7LCKCM9Lh4hEb4pTiSYUGDPWEBw86d690N1Nx1ORP8NnXE1DR6IXvc5Hl2vGRLQMK_esaajEpwEAYTfpQCuFYR3AjxW4rj7CH7r6OHzEpfZChCKUNkZEgzOiTIrFWf9RDZ8KHKSpeNUhACBZ2ljmQJgCM-UGFrEWV9vcd-WA8OE1saNrOauyzuNYsXRXWuCuW1VFYpLf_249t10sjI3NLqJ-JenGZftRshQ8xeIgaS5ZxzUztGtxk61wdNcVJN3yY5hdGzG_H54aU-aShPaZvjEJI4g'

# Headers
headers = {
  'Accept': 'application/json',
  'Authorization': access_token
}

# Base URL
base_url = "https://graph.microsoft.com/v1.0/users?$filter=startswith(userPrincipalName, '{letter}') or startswith(displayName, '{letter}') or startswith(mail, '{letter}')&$top=999"

# List to store results
all_users = []

# Loop through each letter in the alphabet
for letter in string.ascii_lowercase:
    print(f"Fetching data for letter: {letter.upper()}")  # Log for each letter
    url = base_url.format(letter=letter)
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        # Add the users to the list
        all_users.extend(data.get('value', []))
        print(f"Successfully fetched {len(data.get('value', []))} users for letter: {letter.upper()}")
        
        # Handle pagination if there's a nextLink
        while '@odata.nextLink' in data:
            next_link = data['@odata.nextLink']
            response = requests.get(next_link, headers=headers)
            if response.status_code == 200:
                data = response.json()
                users_fetched = len(data.get('value', []))
                all_users.extend(data.get('value', []))
                print(f"Fetched additional {users_fetched} users for letter: {letter.upper()} from nextLink")
            else:
                print(f"Failed to fetch data for nextLink with status code: {response.status_code}")
                break
    else:
        print(f"Failed to fetch data for letter '{letter.upper()}' with status code: {response.status_code}")

# Convert to DataFrame
df = pd.DataFrame(all_users)

# Save to Excel
df.to_excel('users_data.xlsx', index=False)
print("Data has been exported to 'users_data.xlsx'")

