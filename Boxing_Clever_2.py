from boxsdk import JWTAuth
from boxsdk import Client

def main():
    client_info = set_connection()
    print(client_info)
    print("before getting data")
    get_data(client_info)
    print("after getting data")

def set_connection():
    auth = JWTAuth.from_settings_file('C:\\Users\\gwilliams\\Desktop\\Python Experiments\\work projects\\Working_with_Box\\Working_with_Box\\config_info\\keys_config.json')
    
    client = Client(auth)
    
    return client


def get_data(client):
    print("start of get data")
    
    root_folder = client.root_folder().get()
    print(type(root_folder))

    print(root_folder)

    items = root_folder.get_items()

    #for item in items:
    #    print(f"{item.type.capitalize()} {item.id} is named {item.name}")
    #    with open (item.name, 'wb') as open_file:
    #        client.file(item.id).download_to(open_file)
    #        open_file.close()


if __name__ == "__main__":
    main()