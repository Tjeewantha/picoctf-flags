import base64

base64_string = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg=="
times = 2

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = []

def base64_decoder(string, t):
	i=1
	while i <= t:
		decoded_string = base64.b64decode(string).decode('utf-8')
		new_decode_string = decoded_string[2:-2]
		string = new_decode_string
		i += 1

	return decoded_string

def cal(list):
	current_index = list.index(letter)
	root_index = current_index + 19
	if root_index >= 26:
		decrypt_index = root_index - 26
	else:
		decrypt_index = root_index

	return decrypt_index


for l in lowercase:
	uppercase.append(l.upper())

encrypted_string = base64_decoder(base64_string, times)
decrypted_string = ""

for letter in encrypted_string:
	if letter in lowercase:
		decrypted_value = lowercase[cal(lowercase)]
		decrypted_string += decrypted_value
	elif letter in uppercase:
		decrypted_value = uppercase[cal(uppercase)]
		decrypted_string += decrypted_value
	else:
		decrypted_string += letter


print(decrypted_string)