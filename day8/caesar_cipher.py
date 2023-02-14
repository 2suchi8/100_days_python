alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


 
def caesar(start_text,shift_val,cipher_direction):
  end_text=""
  if cipher_direction=="decode":
      shift_val*=-1
  for i in start_text:
    if i in alphabet:
      pos=alphabet.index(i)
      new_pos=pos+shift_val
      end_text+=alphabet[new_pos]
    else:
        end_text+=i
  print(f"Here's the {direction}d result: {end_text}")


  
"""def encrypt(plain_text,shift_val):
  cipher_text=""
  for i in plain_text:
    pos=alphabet.index(i)
    new_pos=pos+shift_val 
    new_let=alphabet[new_pos]
    cipher_text+=new_let
  print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text,shift_val):
  plain_text=""
  for i in cipher_text:
    pos=alphabet.index(i)
    new_pos=pos-shift_val 
    new_let=alphabet[new_pos]
    plain_text+=new_let
  print(f"The encoded text is {plain_text}")

if direction=="encode":
  encrypt(plain_text=text,shift_val=shift)
elif direction=="decode":
  decrypt(cipher_text=text,shift_val=shift)
"""
should_continue=True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=shift%25
  caesar(start_text=text,shift_val=shift,cipher_direction=direction)
  result=input("Do you want to continue? 'yes' to confirm. 'no' to stop.")
  if result=="no":
    should_continue=False
    print("Goodbye")
  

  