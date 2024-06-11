#!python3

#Sometimes super long oneliner payloads get messed up
#This will split your payload and add small pauses to catch up

payload = "Your_payload_here" 
n = 50
for i in range(0, len(payload), n):
    print("Q STRING " + payload[i:i+n])
    print("Q DELAY 200")
    