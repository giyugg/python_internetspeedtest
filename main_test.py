import speedtest

def list_servers():
    st = speedtest.Speedtest()
    servers_dict = st.get_servers()  # Retrieves a dictionary of available servers
    server_list = []

    print("\nAvailable servers:")

    # Flatten the dictionary into a list for easy indexing
    for server_list_group in servers_dict.values():
        for server in server_list_group:
            server_list.append(server)
            print(f"{len(server_list)}: {server['host']} - {server['country']} ({server['name']})")

def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download()
    upload_speed = st.upload()
    ping = st.results.ping

    download_speed_value = download_speed / 1_000_000
    upload_speed_value = upload_speed / 1_000_000

    print(f"Ping: {ping} ms")
    print(f"Download Speed: {download_speed_value:.2f} mbps")
    print(f"Upload Speed: {upload_speed_value:.2f} mbps")

def main():
    while True:
        print("\nMenu:")
        print("1. Check available servers")
        print("2. Test internet speed")
        print("3. Exit")

        choice = input("\nEnter your choice (1/2/3): ")

        if choice == '1':
            list_servers()  # List available servers
        elif choice == '2':
            print("\nDo you want to:")
            print("1. Automatically select the best server")
            print("2. Manually choose a server")
            server_choice = input("\nEnter your choice (1/2): ")

            if server_choice == '1':
                # Automatically select the best server
                test_speed()
            elif server_choice == '2':
                # List servers and let the user pick one
                servers = list_servers()  # Ensure this returns the list of servers
                print(f"DEBUG - Servers retrieved: {servers}")  # Debugging line
                if servers:  # Check if servers are available
                    selected_index = int(input("\nEnter the server number you want to test: ")) - 1

                    if 0 <= selected_index < len(servers):
                        selected_server = servers[selected_index]
                        test_speed(selected_server)
                    else:
                        print("Invalid server selection.")
                else:
                    print("No servers available.")
            else:
                print("Invalid choice.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
