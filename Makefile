# ssdsim linux support


# 定义编译器和编译选项
CC = gcc
CFLAGS = -g -c

# 定义目标文件
OBJS = ssd.o avlTree.o flash.o initialize.o pagemap.o hash_table.o
TARGET = ssd

# 默认目标
all: $(TARGET)

# 链接目标文件生成可执行文件
$(TARGET): $(OBJS)
	$(CC) -g -o $(TARGET) $(OBJS)

# 定义各个目标文件的规则
ssd.o: ssd.c flash.h initialize.h pagemap.h
	$(CC) $(CFLAGS) ssd.c

flash.o: flash.c pagemap.h
	$(CC) $(CFLAGS) flash.c

initialize.o: initialize.c avlTree.h pagemap.h
	$(CC) $(CFLAGS) initialize.c

pagemap.o: pagemap.c initialize.h hash_table.h
	$(CC) $(CFLAGS) pagemap.c

avlTree.o: avlTree.c
	$(CC) $(CFLAGS) avlTree.c

# 清理规则
clean:
	rm -f $(TARGET) $(OBJS) *~
.PHONY: clean

