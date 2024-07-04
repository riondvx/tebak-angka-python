import random

print("=== Tebak Angka ===")
print("")

istart = 1
iend = 100
is_valid_answer = False
computer_number = random.randint(istart, iend)

print(f"Saya memilih angka antara {istart} sampai {iend}. Coba tebak!")

while not is_valid_answer:
  user_answer = int(input("Masukkan tebakan Anda: "))

  if user_answer == computer_number:
    print(f"Tebakan Benar! Angka yang saya pilih adalah {computer_number}.")
    is_valid_answer = True
  elif user_answer < computer_number:
    print("Terlalu rendah!")
  else:
    print("Terlalu tinggi!")
