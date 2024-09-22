import os
import speedtest
import time

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
    
    return server_list  # Return the list of servers

def save_to_file(directory, filename, content):
    # Ensure the directory exists, create if not
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Append '.txt' extension if not provided
    if not filename.endswith(".txt"):
        filename += ".txt"

    # Create the full path for the file
    file_path = os.path.join(directory, filename)

    # Write the content to the file
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"\nResults saved to {file_path}\n")

def test_speed(selected_server=None):
    st = speedtest.Speedtest()

    # Start timer (initialize start_time for both automatic and manual selection)
    start_time = time.time()

    if selected_server:
        # Manually select the server
        st.get_servers([selected_server['id']])  # Provide the server ID to filter
        st.get_best_server([selected_server])    # Select the best server from the filtered list
    else:
        # Automatically select the best server
        st.get_best_server()
    
    print("\nStarting speed test...\n")

    for i in range(1, 6):  # A loop to simulate progress (count from 1 to 5)
        print(f"Progress: {i}/5 ...")
        time.sleep(3)  # Simulate the time delay for each step in progress

    # Test download and upload speed
    download_speed = st.download()
    upload_speed = st.upload()
    ping = st.results.ping

    # Stop timer
    end_time = time.time()
    elapsed_time = end_time - start_time

    download_speed_value_kbps = download_speed / 1_000
    upload_speed_value_kbps = upload_speed / 1_000
    download_speed_value_mbps = download_speed / 1_000_000
    upload_speed_value_mbps = upload_speed / 1_000_000
    download_speed_value_gbps = download_speed / 1_000_000_000
    upload_speed_value_gbps = upload_speed / 1_000_000_000

    # Display time taken to perform the speed test
    result_content = (
        f"Time taken for the speed test: {elapsed_time:.2f} seconds\n\n"
        f"Ping: {ping} ms\n\n"
        f"Download Speed in KBPS: {download_speed_value_kbps:,.2f} kbps\n"
        f"Upload Speed in KBPS: {upload_speed_value_kbps:,.2f} kbps\n\n"
        f"Download Speed in MBPS: {download_speed_value_mbps:,.2f} mbps\n"
        f"Upload Speed in MBPS: {upload_speed_value_mbps:,.2f} mbps\n\n"
        f"Download Speed in GBPS: {download_speed_value_gbps:,.2f} gbps\n"
        f"Upload Speed in GBPS: {upload_speed_value_gbps:,.2f} gbps\n"
    )

    print(result_content)

    # Ask the user if they want to save the results to a file
    save_option = input("Do you want to save the results to a file? (y/n): ").lower()

    if save_option == 'y':
        directory = input("Enter the directory to save the file (e.g., /path/to/directory): ")
        filename = input("Enter the filename (e.g., speed_test_results.txt): ")

        # Save the results to the specified file
        save_to_file(directory, filename, result_content)

def main():
    while True:
        print("Menu:")
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