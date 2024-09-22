import os
from datetime import datetime
import pytz

# Function to get the current time with timezone
def get_current_time_with_timezone():
    # Replace 'YOUR_TIMEZONE' with the actual timezone, e.g., 'US/Eastern'
    tz = pytz.timezone('Philippines')
    now = datetime.now(tz)
    return now.strftime("%Y-%m-%d %H:%M:%S %Z")

# Enhanced function to save the speed test results with the date and time
def save_test_results_with_time(directory, filename, content):
    # Get the current time with timezone
    current_time = get_current_time_with_timezone()
    
    # Append the time info to the content
    content_with_time = f"Speed test performed on: {current_time}\n\n" + content

    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Append .txt if not provided
    if not filename.endswith(".txt"):
        filename += ".txt"

    # Save the content to the file
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w') as f:
        f.write(content_with_time)

    print(f"\nResults saved to {file_path}\n")