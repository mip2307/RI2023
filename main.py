N = 31;
hash_table = [[] for _ in range(N)];

def hash_function(key):
    return key % N

def insert(key, value):
    hash_key = hash_function(key)
    bucket = hash_table[hash_key]
    found_key = False

    for index, record in enumerate(bucket):
        record_key, record_val = record

        if record_key == key:
            found_key = True
            break

        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

def search(key):
    skey = hash_function(key)
    bucket = hash_table[skey]
    found_key = False

    for index, record in enumerate(bucket):
        record_key, record_val = record

        if record_key == key:
            found_key = True
            break

        if found_key:
            return record_key
        else:
            return 'Cheia nu a fost gasita'

