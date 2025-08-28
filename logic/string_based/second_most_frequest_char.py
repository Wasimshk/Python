# Find the second most frequent character in a string.

s = "Finnwd the snewcwonnd most freqnwuwent chwarwnacwter iwn a stnriwng."

d = {}

for ch in s:
    if ch not in d:
        d[ch] = 1
    else:
        d[ch] += 1
print(d)

ch1 = ch2 = None
count1 = count2 = 0

for ch, count in d.items():
    if count1 < count:
        ch2 = ch1
        count2 = count1

        count1 = count
        ch1 = ch
    elif count2 < count and count1 != count2:
        count2 = count
        ch2 = ch

print(f"The second most char is: '{ch2}' with total {count2} count")


