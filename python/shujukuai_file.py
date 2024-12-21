def process_trace(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    num = 0
    num_write = 0
    read_size=0
    write_size=0
    prev_addr = 0
    prev_size = 0
    pre_addr_write = 0
    pre_size_write = 0

    with open(output_file, 'w') as f_out:
        for i in range(len(lines)):
            line = lines[i].split()
            user = line[1]
            addr = int(line[2])
            size = int(line[3])
            operation = int(line[4])
            #print(user,addr,size,operation)

            if operation == 1:
                pre_addr_write = 0
                pre_size_write = 0
                read_size+=size
                if i > 0 and addr == prev_addr + prev_size:
                    f_out.write(lines[i].rstrip() + f' {num}\n')
                else:
                    num += 1
                    f_out.write(lines[i].rstrip() + f' {num}\n')
                prev_addr = addr
                prev_size = size
            else:
                prev_addr = 0
                prev_size = 0
                write_size+=size
                if i > 0 and addr == pre_addr_write + pre_size_write:
                    f_out.write(lines[i].rstrip() + f' {num_write}\n')
                else:
                    num_write += 1
                    f_out.write(lines[i].rstrip() + f' {num_write}\n')
                pre_addr_write = addr
                pre_size_write = size

    average_read_size=read_size/num
    average_write_size=write_size/num_write
    print("average read size= ",average_read_size,"average write size= ",average_write_size)
    print("read num= ",num," write num= ",num_write)

if __name__ == "__main__":
    input_file = "/home/ywy/disk/data_fad/mails/mail4_d.trace"
    output_file = "/home/ywy/disk/data_fad/mails/nodedup_mail_file4.trace"

    process_trace(input_file, output_file)
