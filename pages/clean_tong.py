import subprocess

# Install Streamlit and pyngrok if not already installed
!pip install streamlit pyngrok -q

# Run the Streamlit app in the background
# This will provide a public URL via ngrok
print('🚀 Launching Streamlit App...')

# Terminate any existing Streamlit processes to prevent conflicts
subprocess.run(['killall', 'streamlit'], capture_output=True, text=True, check=False)

# Run the Streamlit app and tunnel it with ngrok
# The output will include the ngrok URL
!streamlit run clean_app.py &>/dev/null& # run in background

import time
import re

time.sleep(5) # Give some time for ngrok to start

# Use 'pgrep' to find the ngrok process and 'grep' to filter for 'http://'
# This is a common way to get the URL in Colab when ngrok is running in the background
def get_ngrok_url():
    try:
        # Look for ngrok URLs in the ngrok log file or processes
        # A common way is to check the output of `ngrok tunnel list` or `ngrok http` if run in foreground
        # For background process, we often rely on stdout if redirected or log files
        
        # Attempt to read ngrok's output if it was redirected or search system logs/process output
        # A robust way is to run `ngrok http --log stdout ...` and capture that stdout
        
        # For simplicity in Colab, sometimes the URL is accessible via a specific port and a web request
        # Or by checking system logs or a temporary file created by ngrok
        
        # A common workaround is to use 'curl' against the ngrok API endpoint
        response = subprocess.run(['curl', '-s', 'http://localhost:4040/api/tunnels'], capture_output=True, text=True, check=True)
        tunnels_info = response.stdout
        # Extract the public URL
        match = re.search(r'"public_url":"(https://[^"]+)"', tunnels_info)
        if match:
            return match.group(1)
    except Exception as e:
        return f"Error getting ngrok URL: {e}"
    return "Ngrok URL not found. Please check if ngrok is running correctly."

ngrok_url = get_ngrok_url()
print(f"🎉 Your Streamlit app is live at: {ngrok_url}")
