############################### START ALTERNATIVE CODE FOR IMAGE ENCRYPTION & DECRYPTION HERE #####################
import pyAesCrypt
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "foopassword"
# encrypt
pyAesCrypt.encryptFile("test.png", "test(enecrypted).png", password, bufferSize)
# decrypt
pyAesCrypt.decryptFile("test(enecrypted).png", "testout.png", password, bufferSize)
###########################ENDS HERE ###############################