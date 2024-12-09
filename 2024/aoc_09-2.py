from common import get_input_lines, print_list

def expand_diskmap(diskmap:list)->tuple:
    disk = []
    file_blocks = [] # (address, size)
    free_blocks = [] # (address, size)

    for index in range(len(diskmap)):
        if not index % 2: # It's a file
            file_blocks.append((len(disk), diskmap[index]))
            disk += [index//2] * diskmap[index]
        else: # It's free space
            free_blocks.append((len(disk), diskmap[index]))
            disk += ['.'] * diskmap[index]
    return (disk, file_blocks, free_blocks)

def compact_disk(disk:list, file_blocks:list, free_blocks:list)->list:
    for file in file_blocks[::-1]:
        for free in free_blocks:
            if free[0] > file[0]:
                # Only move files left
                break
            if free[1] >= file[1]:
                # swap file to free space
                for x in range(file[1]):
                    disk[free[0] + x], disk[file[0] + x] = disk[file[0] + x], disk[free[0] + x]
                # update free_blocks
                if free[1] == file[1]:
                    free_blocks.pop(free_blocks.index(free))
                else:
                    free_blocks[free_blocks.index(free)] = (free[0] + file[1], free[1] - file[1])
                break

    return disk

def compute_checksum(disk:list)->int:
    return sum(idx * entry for idx, entry in enumerate(disk) if entry != '.')

def main():
    diskmap = [int(x) for x in get_input_lines('aoc_09.txt')[0]]
    
    (disk, file_blocks, free_blocks) = expand_diskmap(diskmap)
    compacted = compact_disk(disk, file_blocks, free_blocks)
    checksum = compute_checksum(compacted)

    print(f'The filesystem checksum is {checksum}')

if __name__ == '__main__':
    main()