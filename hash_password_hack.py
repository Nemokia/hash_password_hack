import hashlib
import csv


def hash_password_hack(input_file_name, output_file_name):
    from hashlib import sha256

    with open(input_file_name) as fin:
        reader = csv.reader(fin)
        hash_numb = {}
        hacked_pass = {}

        for digit_numb in range(1000, 9999):
            in_file_hash = sha256(str(digit_numb).encode()).hexdigest()
            hash_numb[in_file_hash] = digit_numb

        for name_and_hash in reader:
            name_in_reader = name_and_hash[0]
            hash_in_reader = name_and_hash[1]
            for files_hash in hash_numb.keys():
                if hash_in_reader == files_hash:
                    hacked_pass[name_in_reader] = hash_numb.get(files_hash)
        count = 0
    with open(output_file_name, "w") as out:
        for names in hacked_pass:
            count += 1
            if count == 1:
                out.write(names + "," + str(hacked_pass.get(names)))
            else:
                out.write("\n" + names + "," + str(hacked_pass.get(names)))


print(hash_password_hack('input_file_name.csv','output_file_name.csv'))
