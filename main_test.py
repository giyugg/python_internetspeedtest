import os
import speedtest
import time
import socket

def test_speed(selected_server=None):
    st = speedtest.Speedtest()

    # Start timer (initialize start_time for both automatic and manual selection)
    start_time = time.time()

    # Fetch client IP address
    client_ip = socket.gethostbyname(socket.gethostname())
    
    if selected_server:
        # Manually select the server
        st.get_servers([selected_server['id']])  # Provide the server ID to filter
        best_server = st.get_best_server([selected_server])    # Select the best server from the filtered list
    else:
        # Automatically select the best server
        best_server = st.get_best_server()

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

    # Server IP address
    server_ip = best_server['host']

    # Display time taken and IP addresses
    result_content = (
        f"Client IP Address: {client_ip}\n"
        f"Server IP Address: {server_ip}\n\n"
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
