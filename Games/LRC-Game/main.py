# Function to calculate the LRC for a list of binary strings
def calculate_lrc(segments):
    lrc = [0] * 8  # Initialize LRC to 8 zeros

    for segment in segments:
        for i, bit in enumerate(segment):
            lrc[i] += int(bit)

    for i in range(8):
        lrc[i] %= 2  # Take modulo 2 to determine even or odd

    # Check if LRC is even, set VRC to 0; if LRC is odd, set VRC to 1
    vrc = 0 if sum(lrc) % 2 == 0 else 1

    # Return the updated LRC with the VRC
    return lrc + [vrc]

# Input: Number of segments
n = int(input())
segments = []

# Input: Binary segments
for _ in range(n):
    segments.append(input().strip())

# Input: LRC for Receiver
receiver_lrc = list(map(int, input().strip()))

# Calculate LRC for Sender
sender_lrc = calculate_lrc(segments)

# Check if LRCs match
if sender_lrc == receiver_lrc:
    print("Rejected")
else:
    print("Data accepted")
