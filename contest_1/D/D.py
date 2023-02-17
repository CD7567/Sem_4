from sys import stdout

def GetDist(x, y):
    print('?', x, y, '\n')
    stdout.flush()
    return int(input())

ld_angle_dist = GetDist(-1_000_000, -1_000_000)
lu_angle_dist = GetDist(-1_000_000, 1_000_000)

print('!', (ld_angle_dist + lu_angle_dist - 4_000_000) // 2, (ld_angle_dist - lu_angle_dist) // 2, '\n')