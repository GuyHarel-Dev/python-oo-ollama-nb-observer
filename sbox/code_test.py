import httpx

def test():
    client = httpx.Client()
    response = client.get('https://example.org')
    print(response)

if __name__ == "__main__":
    test()

    

