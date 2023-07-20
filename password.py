import maskpass 
if __name__ == "__main__":
    username = input("enter username: ")


pwd = maskpass.askpass(mask="*")

print (username)
print (pwd)

#