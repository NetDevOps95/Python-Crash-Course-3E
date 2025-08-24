guest_list = ['danny', 'trudy', 'yaa']

print(f"{guest_list[0].title()} can't make it to the dinner!")

removed_guest ="danny"
guest_list.remove(removed_guest)

guest_list.insert(0, "danny junior")
print(f"{guest_list[0].title()} you are invited to dinner at my house!")
print(f"{guest_list[1].title()} you are invited to dinner at my house!")
print(f"{guest_list[2].title()} you are invited to dinner at my house!")


guest_list.insert(0, "baby k")
guest_list.insert(2, "whitley")
guest_list.insert(5, "kid")

print(guest_list)

print("Unfortunately, I can only invited two people to dinner...")

revoked_invitation_5 = guest_list.pop(5)
print(f"Unfortunately {revoked_invitation_5.title()} you are no longer invited to dinner at my house!\n")

revoked_invitation_4 = guest_list.pop(4)
print(f"Unfortunately {revoked_invitation_4.title()} you are no longer invited to dinner at my house!\n")

revoked_invitation_3 = guest_list.pop(3)
print(f"Unfortunately {revoked_invitation_3.title()} you are no longer invited to dinner at my house!\n")

revoked_invitation_2 = guest_list.pop(2)
print(f"Unfortunately {revoked_invitation_2.title()} you are no longer invited to dinner at my house!\n")

print(f"{guest_list[0].title()} you are still invited to dinner at my house!")
print(f"{guest_list[1].title()} you are still invited to dinner at my house!")

del guest_list[1]
del guest_list[0]

print(guest_list)