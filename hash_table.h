#ifndef HASH_TABLE_H  // 防止重复包含
#define HASH_TABLE_H


// 定义动态哈希表
typedef struct Node {
    char str[50];
    struct Node *next;
} Node;

typedef struct HashTable {
    Node **buckets;   // 哈希表存储桶数组
    int size;         // 当前存储桶数量
    int count;        // 当前已存储的字符串数量
} HashTable;

// 哈希函数（基于djb2）
unsigned int hash(const char *str, int tableSize) ;

// 初始化哈希表
HashTable *initHashTable(int initialSize) ;

// 检查字符串是否已存在
int contains(HashTable *table, const char *str) ;


// 重新分布哈希表（扩展容量）
void rehash(HashTable *table) ;

// 插入字符串到哈希表
int addString(HashTable *table, const char *str) ;

// 释放哈希表内存
void freeHashTable(HashTable *table) ;



#endif // HASH_TABLE_H
