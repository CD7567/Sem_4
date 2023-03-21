import sys

for line in sys.stdin:
    sha, _, _, _, msg = line.split('\t')
    print('{}{:.>73}'.format(sha[:7], msg.strip()))