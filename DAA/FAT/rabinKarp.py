# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book

# d is the number of characters in the input alphabet
d = 256

# pat -> pattern
# txt -> text
# q -> A prime number


def search(pat, txt, q):
	p_len = len(pat)
	t_len = len(txt)
	i = 0
	match_index = 0
	p_hash = 0 # hash value for pattern
	t_hash = 0 # hash value for txt
	h = 1

	# The value of h would be "pow(d, p_len-1)%q"
	for i in range(p_len-1):
		h = (h*d) % q

	# Calculate the hash value of pattern and first window
	# of text
	for i in range(p_len):
		p_hash = (d*p_hash + ord(pat[i])) % q
		t_hash = (d*t_hash + ord(txt[i])) % q

	# Slide the pattern over text one by one
	for i in range(t_len-p_len+1):
		# Check the hash values of current window of text and
		# pattern if the hash values match then only check
		# for characters one by one
		if p_hash == t_hash:
			# Check for characters one by one
			for j in range(p_len):
				if txt[i+j] != pat[j]:
					break
				else:
					match_index += 1

			# if p_hash == t_hash and pat[0...p_len-1] = txt[i, i+1, ...i+p_len-1]
			if match_index == p_len:
				print(f"Pattern '{txt[i:i+p_len]}' found at index " + str(i))
				return

		# Calculate hash value for next window of text: Remove
		# leading digit, add trailing digit
		if i < t_len-p_len:
			t_hash = (d*(t_hash-ord(txt[i])*h) + ord(txt[i+p_len])) % q

			# We might get negative values of t_hash, converting it to
			# positive
			if t_hash < 0:
				t_hash = t_hash+q
		else:
			print("Match not found")


# Driver Code
if __name__ == '__main__':
    txt = "CATS AND DOGS"
    pat = "DOG"
    q = 101
    print(f"The test is '{txt}'")
    print(f"The pattern is '{pat}'")
    search(pat, txt, q)

