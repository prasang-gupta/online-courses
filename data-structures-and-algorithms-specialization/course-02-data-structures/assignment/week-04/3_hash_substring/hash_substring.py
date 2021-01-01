# python3

_multiplier = 263
_prime = 1000000007

def read_input():
    return input().rstrip(), input().rstrip()

def print_occurrences(output):
    print(' '.join(map(str, output)))

def polyhash(s):
    ans = 0
    for c in reversed(s):
        ans = (ans * _multiplier + ord(c)) % _prime
    return ans

def precomputehashes(text, sizep):
    result = [0] * (len(text) - sizep + 1)
    subset = text[len(text) - sizep:]
    result[len(text) - sizep] = polyhash(subset)
    y = 1
    for i in range(1, sizep + 1):
        y = (y * _multiplier) % _prime
    for i in range((len(text) - sizep - 1), -1, -1):
        result[i] = (((_multiplier * result[i+1]) % _prime) + ord(text[i]) - ((y * ord(text[i + sizep])) % _prime) + _prime) % _prime
    return result
    
def get_occurrences(pattern, text):
    result = []
    phash = polyhash(pattern)
    hashes = precomputehashes(text, len(pattern))
    for i in range(len(text) - len(pattern) + 1):
        if phash != hashes[i]:
            continue
        if text[i : i + len(pattern)] == pattern:
            result.append(i)
    return result

if __name__ == '__main__':
    pattern, text = read_input()
    print_occurrences(get_occurrences(pattern, text))

