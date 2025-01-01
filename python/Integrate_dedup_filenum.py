def process_file(input_file, output_file):
    # 第一遍扫描：记录文件编号出现次数
    read_tracker = {}  # 读操作文件编号计数
    write_tracker = {}  # 写操作文件编号计数

    with open(input_file, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            parts = line.strip().split()
            operation = int(parts[4])  # 操作类型（读/写）
            file_num = int(parts[6])  # 文件编号

            # 根据操作类型更新对应容器
            if operation == 1:  # 读操作
                read_tracker[file_num] = read_tracker.get(file_num, 0) + 1
            else:  # 写操作
                write_tracker[file_num] = write_tracker.get(file_num, 0) + 1

    # 第二遍扫描：处理文件编号
    readnum = 0  # 初始读操作编号
    writenum = 0  # 初始写操作编号
    prev_operation = -1
    prev_file_num = -1

    with open(output_file, 'w') as outfile:
        for i, line in enumerate(lines):
            parts = line.strip().split()
            time, device, lsn, size, operation, md5, file_num = (
                int(parts[0]),
                int(parts[1]),
                int(parts[2]),
                int(parts[3]),
                int(parts[4]),
                parts[5],
                int(parts[6]),
            )
            new_file_num = 0

            if prev_operation == -1:
                if operation == 1:
                    readnum+=1
                    new_file_num = readnum
                else :
                    writenum+=1
                    new_file_num = writenum
                prev_operation = operation
                prev_file_num = file_num
            else:
                if prev_operation == operation:
                    if operation == 1:
                        if file_num == prev_file_num:
                            new_file_num = readnum
                        else: 
                            if read_tracker[prev_file_num] != 1:
                                readnum+=1
                                new_file_num = readnum
                            else:
                                if read_tracker[file_num] != 1:
                                    readnum+=1
                                    new_file_num = readnum
                                else:
                                    new_file_num = readnum
                    if operation == 0:
                        if file_num == prev_file_num:
                            new_file_num = writenum
                        else: 
                            if write_tracker[prev_file_num] != 1:
                                writenum+=1
                                new_file_num = writenum
                            else:
                                if write_tracker[file_num] != 1:
                                    writenum+=1
                                    new_file_num = writenum
                                else:
                                    new_file_num = writenum
                else:
                    if operation == 1:
                        readnum +=1
                        new_file_num = readnum
                    else :
                        writenum+=1
                        new_file_num = writenum

            # 写入处理后的行
            outfile.write(f"{time} {device} {lsn} {size} {operation} {md5} {new_file_num}\n")

            # 更新上一行的信息
            prev_operation = operation
            prev_file_num = file_num


# 输入输出文件名
input_filename = "/home/ywy/FAD-SSDsim/data/web/nodedup-webvm_file.trace"
output_filename = "/home/ywy/FAD-SSDsim/data/web/2_nodedup-webvm_file.trace"

# 调用函数处理文件
process_file(input_filename, output_filename)
