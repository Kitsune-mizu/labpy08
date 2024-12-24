nama_lengkap = input("Masukkan nama lengkap: ")
nomor_telepon = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

valid = True
errors = []

# Validasi nama lengkap
if not nama_lengkap.isalpha():
    valid = False
    errors.append("Nama lengkap harus hanya berisi huruf.")

# Validasi nomor telepon
if not nomor_telepon.isdigit():
    valid = False
    errors.append("Nomor telepon harus hanya berisi angka.")

# Validasi email
if "@" not in email or "." not in email:
    valid = False
    errors.append("Email harus mengandung karakter '@' dan '.'.")

# Hasil validasi
if valid:
    print("Data pendaftaran valid.")
else:
    print("Data pendaftaran tidak valid:")
    for error in errors:
        print(f"- {error}")
