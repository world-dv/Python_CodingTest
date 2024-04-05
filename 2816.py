import sys
N = int(sys.stdin.readline().rstrip())
channel = []
for _ in range(N):
    channel.append(sys.stdin.readline().rstrip())


def switchChannel(target, target_idx, start_idx, number):
    idx = start_idx
    while channel[target_idx] != target:
        if channel[idx] != target:
            number += '1'
            idx += 1
        else:
            number += '4'
            channel[idx-1], channel[idx] = channel[idx], channel[idx-1]
            idx -= 1
    return number


print(switchChannel('KBS1', 0, 0, '') + switchChannel('KBS2', 1, 0, ''))
