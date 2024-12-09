from common import get_input_lines

def expand_diskmap(diskmap:list)->list:
    disk = []
    file_no = 0

    for index in range(len(diskmap)):
        if not index % 2: # It's a file
            for x in range(diskmap[index]):
                disk.append(file_no)
            file_no += 1
        else: # It's free space
            for x in range(diskmap[index]):
                disk.append('.')
    return disk

def compact_disk(disk:list)->list:
    left_idx, right_idx = 0, len(disk) - 1

    while left_idx < right_idx:
        if not '.' == disk[left_idx]:
            left_idx += 1
        elif '.' == disk[right_idx]:
            right_idx -= 1
        else:
            disk[left_idx], disk[right_idx] = disk[right_idx], disk[left_idx]
            left_idx += 1
            right_idx -= 1

    return disk

def compute_checksum(disk:list)->int:
    checksum = 0
    for idx in range(len(disk)):
        if '.' == disk[idx]:
            break
        checksum += idx * disk[idx]
    return checksum

def main():
    diskmap = [int(x) for x in get_input_lines('aoc_09.txt')[0]]
    
    disk = expand_diskmap(diskmap)
    compacted = compact_disk(disk)
    checksum = compute_checksum(compacted)

    print(f'The filesystem checksum is {checksum}')

if __name__ == '__main__':
    main()
