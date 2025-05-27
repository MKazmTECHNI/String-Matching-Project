import time  # thats gunna be used to measure the time it takes to run the code


def levenshteinDistance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]  # cool 2D matrix to store distances
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]


# this is in case someone does like Vladmir von Levenshtein
surname_particles = {
    "von",
    "van",
    "de",
    "da",
    "del",
    "di",
    "la",
    "le",
    "du",
    "dos",
    "das",
    "der",
    "den",
    "ter",
    "ten",
    "el",
    "al",
    "bin",
    "ibn",
    "ap",
    "af",
    "mac",
    "mc",
    "fitz",
    "st.",
    "saint",
}

input_parts = input("Enter the name and surname: ").split()

if len(input_parts) == 2:
    inputed_name, inputed_surname = input_parts
else:
    particle_idx = None
    for idx, part in enumerate(input_parts[1:], 1):
        if part.lower() in surname_particles:
            particle_idx = idx
            break
    if particle_idx is not None:
        inputed_name = " ".join(input_parts[:particle_idx])
        inputed_surname = " ".join(input_parts[particle_idx:])
    else:
        inputed_name = input_parts[0]
        inputed_surname = " ".join(input_parts[1:])

print(str(inputed_name), str(inputed_surname))

from names import names
from surnames import surnames

if (
    inputed_name not in names
    and inputed_surname not in surnames
    and inputed_surname in names
    and inputed_name in surnames
):
    inputed_name, inputed_surname = inputed_surname, inputed_name

if inputed_name not in names and inputed_surname not in surnames:
    min_name_dist = min((levenshteinDistance(inputed_name, n), n) for n in names)
    min_surname_dist = min(
        (levenshteinDistance(inputed_surname, s), s) for s in surnames
    )
    total_dist = min_name_dist[0] + min_surname_dist[0]
    min_name_dist_swapped = min(
        (levenshteinDistance(inputed_surname, n), n) for n in names
    )
    min_surname_dist_swapped = min(
        (levenshteinDistance(inputed_name, s), s) for s in surnames
    )
    total_dist_swapped = min_name_dist_swapped[0] + min_surname_dist_swapped[0]
    if total_dist_swapped < total_dist:
        inputed_name, inputed_surname = inputed_surname, inputed_name

matching_names = {}
last_name_distance = float("inf")
last_surname_distance = float("inf")
final_name = inputed_name
final_surname = inputed_surname

start_time = time.time()

if not inputed_name in names:
    for name in names:
        # print(name)
        new_distance = levenshteinDistance(inputed_name, name)
        if last_name_distance > new_distance:
            last_name_distance = new_distance
            final_name = name

if not inputed_surname in surnames:
    for surname in surnames:
        # print(surname)
        newer_distance = levenshteinDistance(inputed_surname, surname)
        if last_surname_distance > newer_distance:
            last_surname_distance = newer_distance
            final_surname = surname

final_time = time.time()

print()
print("Inputted name =", inputed_name, "Inputted surname =", inputed_surname)
print(final_name, last_name_distance)
print(final_surname, last_surname_distance)


print("~Time it took: ", round(final_time - start_time, 5))
# for matching_name in matching_names:
# print("Levenshtein Distance:", distance)
