#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

#define MAX_NAME 256
#define TABLE_SIZE 10           //can be resize
#define DELETED_NODE (person*)(0xFFFFFFFFFFFFFFFFUL)

typedef struct {
    char name[MAX_NAME];
    int age;
}person;

person * hash_table[TABLE_SIZE];

//hash function(gives a value to every name)
//open addressing - put every data in table, look for available bucket
//deal with collison : open addressing or external chaining w open addressing
unsigned int hash(char *name) {
    int length = strlen(name);
    unsigned int hash_value = 0;
    for (int i = 0; i < length; i++) {
        hash_value += name[i];
        hash_value = hash_value * name[i];
    }

    return hash_value % TABLE_SIZE;
}

//initialize hash table
void init_hash_table() {
    for (int i = 0; i < TABLE_SIZE; i++) {
        hash_table[i] = NULL;
    }
    //table is empty
}

//see names in table
void print_table() {
    printf("start\n");
    for (int i = 0; i < TABLE_SIZE; i++) {
        if (hash_table[i] == NULL) {
            printf("\t%i\t---\n", i);
        } else if (hash_table[i] == DELETED_NODE) {
            printf("\t%i\t---<deleted>\n", i);
        }else {
            printf("\t%i\t%s\n", i, hash_table[i]->name);
        }
    }
    printf("end\n");
}

//insert name into table
bool hash_table_insert(person *p) {
    if (p == NULL)
    {
        return false;
    }
    int index = hash(p->name);
    //linear probing
    for(int i = 0; i < TABLE_SIZE; i++) {
        int try = (i + index) % TABLE_SIZE;
        if(hash_table[try] == NULL || hash_table[try] == DELETED_NODE) {
            hash_table[try] = p;
            return true;
        }
    }

    /*
    if(hash_table[index] != NULL) {
        return false;
    }
    hash_table[index] = p;
    */

    return false;
}

//find a person in the table by their name
person *hash_table_lookup ( char *name) {
    int index = hash(name);
    for (int i = 0; i < TABLE_SIZE; i++) {
        int try = (index + i) % TABLE_SIZE;
        if (hash_table[try] ==  NULL) {
            return false; //not here
        }
        if (hash_table[try] == DELETED_NODE) continue;
        if(strcmp(hash_table[index]->name, name)==0) {
            return hash_table[try];
        }
    }
    return NULL;
}

//delete name in table
person *hash_table_delete(char *name) {
    int index = hash(name);
    for (int i = 0; i < TABLE_SIZE; i++) {
        int try = (index + i) % TABLE_SIZE;
        if (hash_table[try] == NULL) return NULL;
        if (hash_table[try] == DELETED_NODE) continue;
        if(strcmp(hash_table[index]->name, name)==0) {

            person* tmp = hash_table[try];
            hash_table[try] = DELETED_NODE;
            return tmp;
        }
    }
    return NULL;
}

int main(void)
{

    init_hash_table();
    print_table();

    person jacob = {.name="Jacob", .age=25};
    person natalie = {.name="Natalie", .age=17};
    person adam = {.name="Adam", .age=22};
    person taylor= {.name="Taylor", .age=28};
    person sara= {.name="Sara", .age=15};
    person robert= {.name="Robert", .age=35};
    person eliza= {.name="Eliza", .age=39};
    person jane= {.name="Jane", .age=72};
    person kate= {.name="Kate", .age=21};
    person mpho= {.name="Mpho", .age=24};
    person edna= {.name="Edna", .age=33};

    hash_table_insert(&jacob);
    hash_table_insert(&natalie);
    hash_table_insert(&adam);
    hash_table_insert(&taylor);
    hash_table_insert(&sara);
    hash_table_insert(&robert);
    hash_table_insert(&eliza);
    hash_table_insert(&jane);
    hash_table_insert(&kate);
    hash_table_insert(&mpho);
    hash_table_insert(&edna);
    print_table();

    person *tmp = hash_table_lookup("Adam");

    if(tmp == NULL) {
        printf("Not found\n");
    } else {
        printf("Found %s\n", tmp->name);
    }

    tmp = hash_table_lookup("Jacob");

    if(tmp == NULL) {
        printf("Not found\n");
    } else {
        printf("Found %s\n", tmp->name);
    }

    hash_table_delete("Jacob");
    tmp = hash_table_lookup("Jacob");

    if(tmp == NULL) {
        printf("Not found\n");
    } else {
        printf("Found %s\n", tmp->name);
    }


    /*printf("Jacob => %u\n", hash("Jacob"));
    printf("Natalie => %u\n", hash("Natalie"));
    printf("Joe => %u\n", hash("Joe"));
    printf("Bill => %u\n", hash("Bill"));
    printf("Adam => %u\n", hash("Adam"));
    printf("Taylor => %u\n", hash("Taylor"));
    printf("Malcolm => %u\n", hash("Malcolm"));
    */

    return 0;

}