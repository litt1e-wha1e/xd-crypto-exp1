import hashlib
import itertools
import datetime

target_hash = "67ae1a64661ac8b4494666f58c4822408dd0a3e4"
char_groups = [['Q', 'q'], ['W', 'w'], ['%', '5'], ['8', '('], ['=', '0'], ['I', 'i'], ['*', '+'], ['n', 'N']]


def generate_sha1_hash(input_str):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(input_str.encode('utf-8'))
    return sha1_hash.hexdigest()


start_time = datetime.datetime.now()

for combination in itertools.product(*char_groups):
    candidate_str = "".join(combination)

    for permutation in itertools.permutations(candidate_str, 8):
        hashed_value = generate_sha1_hash("".join(permutation))
        if hashed_value == target_hash:
            print("Password found:", "".join(permutation))
            end_time = datetime.datetime.now()
            time_elapsed = (end_time - start_time).total_seconds()
            print(f"Time elapsed: {time_elapsed:.2f} seconds")
            break
    else:
        continue
    break
