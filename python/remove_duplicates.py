# -*- coding: utf-8 -*-
# 打开文件
input_file = "/home/ywy/disk/data_fad/mails/nodedup_mail_file4.trace"  # 输入文件名
output_file = "/home/ywy/disk/data_fad/mails/dedup_mail_file4.trace"  # 输出文件名

# 存储已出现的 md5 值
seen_md5 = set()

# 打开输入文件和输出文件
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        # 分割行，获取最后一列（md5 值）
        parts = line.strip().split()
        if len(parts) < 6:
            continue  # 跳过格式不正确的行
        
        md5 = parts[5]
        ope = int(parts[4])  # 转换操作类型为整数
        if ope == 0:
            if md5 not in seen_md5:
                # 如果是新 md5，则记录并写入输出文件
                seen_md5.add(md5)
                outfile.write(line)
        else:
            outfile.write(line)

print(f"去重完成，结果已保存到 {output_file}")
