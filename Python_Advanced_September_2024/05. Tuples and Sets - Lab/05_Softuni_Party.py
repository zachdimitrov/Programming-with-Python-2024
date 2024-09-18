# num = int(input())
#
# invited_vips = set()
# invited_other = set()
# came_vips = set()
# came_other = set()
#
# for _ in range(num):
#     person = input()
#     if person[0].isdigit():
#         invited_vips.add(person)
#     else:
#         invited_other.add(person)
#
# command = input()
# while command != "END":
#     if command[0].isdigit():
#         came_vips.add(command)
#     else:
#         came_other.add(command)
#     command = input()
#
# vips_not_come = sorted(list(invited_vips.difference(came_vips)))
# other_not_come = sorted(list(invited_other.difference(came_other)))
# print(len(vips_not_come) + len(other_not_come))
# print("\n".join(vips_not_come))
# print("\n".join(other_not_come))


# num = int(input())
#
# invited_vips = set()
# invited_other = set()
#
# for _ in range(num):
#     person = input()
#     if person[0].isdigit():
#         invited_vips.add(person)
#     else:
#         invited_other.add(person)
#
# command = input()
#
# while command != "END":
#     if command[0].isdigit():
#         invited_vips.remove(command)
#     else:
#         invited_other.remove(command)
#     command = input()
#
# print(len(invited_vips) + len(invited_other))
# print("\n".join(sorted(list(invited_vips))))
# print("\n".join(sorted(list(invited_other))))


num = int(input())
invited = set()

for _ in range(num):
    invited.add(input())

command = input()
while command != "END":
    invited.remove(command)
    command = input()

print(len(invited))
print("\n".join(sorted(invited)))


