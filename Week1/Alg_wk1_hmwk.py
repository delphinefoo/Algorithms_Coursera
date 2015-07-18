with open('IntegerArray.txt', 'r') as f:
	nums = f.read().splitlines()
nums = map(int, nums)

counter = 0

def sort_count(list):
	if len(list) < 2:
		return list
	half = len(list) / 2
	return merge(sort_count(list[:half]), sort_count(list[half:]))

def merge(l, r):
	global counter
	final_arr = []
	i = j = 0
	while i < len(l) and j < len(r):
		if l[i] < r[j]:
			final_arr.append(l[i])
			i += 1
		else:
			final_arr.append(r[j])
			counter = counter + (len(l) - i)
			j += 1
	final_arr.extend(l[i:])
	final_arr.extend(r[j:])
	return final_arr

print sort_count(nums)
print counter
	





