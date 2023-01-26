import subprocess

# Define the target URL and wordlist
url = "golpo24.online"
wordlist = "/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt"

# Use gobuster to perform the brute-force attack
result = subprocess.run(["gobuster", "dir", "-u", url, "-w", wordlist, "-t", "50"], capture_output=True)

# Print the output of the attack
print(result.stdout.decode())
