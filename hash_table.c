#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "hash_table.h"  // 包含头文件

/*
// 定义动态哈希表
typedef struct Node {
    char str[50];
    struct Node *next;
} Node;

typedef struct HashTable {
    Node **buckets;   // 哈希表存储桶数组
    int size;         // 当前存储桶数量
    int count;        // 当前已存储的字符串数量
} HashTable;*/

// 哈希函数（基于djb2）
unsigned int hash(const char *str, int tableSize) {
    unsigned int hash = 5381;
    while (*str) {
        hash = ((hash << 5) + hash) + *str++;  // hash * 33 + 当前字符
    }
    return hash % tableSize;
}

// 初始化哈希表
HashTable *initHashTable(int initialSize) {
    HashTable *table = (HashTable *)malloc(sizeof(HashTable));
    table->size = initialSize;
    table->count = 0;
    table->buckets = (Node **)malloc(initialSize * sizeof(Node *));
    for (int i = 0; i < initialSize; i++) {
        table->buckets[i] = NULL;
    }
    return table;
}

// 检查字符串是否已存在
int contains(HashTable *table, const char *str) {
    unsigned int index = hash(str, table->size);
    Node *current = table->buckets[index];
    while (current != NULL) {
        if (strcmp(current->str, str) == 0) {
            return 1;  // 找到，表示已存在
        }
        current = current->next;
    }
    return 0;  // 未找到
}

// 插入字符串到哈希表
int addString(HashTable *table, const char *str);

// 重新分布哈希表（扩展容量）
void rehash(HashTable *table) {
    int oldSize = table->size;
    Node **oldBuckets = table->buckets;

    // 增大哈希表容量为原来的两倍
    table->size *= 2;
    table->count = 0;
    table->buckets = (Node **)malloc(table->size * sizeof(Node *));
    for (int i = 0; i < table->size; i++) {
        table->buckets[i] = NULL;
    }

    // 将旧数据重新插入到新的哈希表中
    for (int i = 0; i < oldSize; i++) {
        Node *current = oldBuckets[i];
        while (current != NULL) {
            addString(table, current->str);
            Node *temp = current;
            current = current->next;
            free(temp);
        }
    }

    free(oldBuckets);
}

// 插入字符串到哈希表
int addString(HashTable *table, const char *str) {
    // 如果字符串已存在，则直接返回
    if (contains(table, str)) {
        return 1;
    }

    // 如果装载因子超过 0.75，则扩展哈希表
    //if ((float)table->count / table->size > 0.75) {
    //    rehash(table);
    //}

    // 计算哈希值并插入新字符串
    unsigned int index = hash(str, table->size);
    Node *newNode = (Node *)malloc(sizeof(Node));
    strcpy(newNode->str, str);
    newNode->next = table->buckets[index];
    table->buckets[index] = newNode;
    table->count++;
    return 2;
}

// 释放哈希表内存
void freeHashTable(HashTable *table) {
    for (int i = 0; i < table->size; i++) {
        Node *current = table->buckets[i];
        while (current != NULL) {
            Node *temp = current;
            current = current->next;
            free(temp);
        }
    }
    free(table->buckets);
    free(table);
}
/*
// 测试程序
int main() {
    HashTable *table = initHashTable(4);  // 初始化哈希表，初始大小为 4

    addString(table, "hello");
    addString(table, "world");
    addString(table, "example");
    addString(table, "hello");  // 重复添加，应该被跳过
    addString(table, "dynamic");

    printf("\"hello\" exists: %d\n", contains(table, "hello"));  // 输出 1
    printf("\"world\" exists: %d\n", contains(table, "world"));  // 输出 1
    printf("\"notfound\" exists: %d\n", contains(table, "notfound"));  // 输出 0

    freeHashTable(table);  // 释放内存
    return 0;
}*/
