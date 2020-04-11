from boxsdk import OAuth2, Client

# code shamelessly ripped from https://stackoverflow.com/questions/29594289/how-to-download-files-with-box-api-python

# JWT authorisation may be the best if this job is run through cron
#  

def main():
    login_info = get_file()
    get_data(login_info)


def get_file():
    auth = OAuth2(
        client_id = '8osue5au0e4qkg067pbajh25wu6ei020',
        client_secret = ' cmowIR0FjZKvFQwpPbVcvqm5B5lkmRFd',
        access_token = 'lo384OfBSz36wNFLe63HcsskhcP2P00w'
        )

    client = Client(auth)

    return client


def get_data(client):

    root_folder = client.root_folder().get()

    print(root_folder)

    items = root_folder.get_items()

    for item in items:
        print(f"{item.type.capitalize()} {item.id} is named {item.name}")
        with open (item.name, 'wb') as open_file:
            client.file(item.id).download_to(open_file)
            open_file.close()


if __name__ == "__main__":
    get_file()