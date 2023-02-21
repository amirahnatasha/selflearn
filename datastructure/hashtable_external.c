//Implement hash table with linked list (External chaining)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

#define MAX_NAME 256
#define TABLE_SIZE 10           //can be resize

typedef struct person{
    char name[MAX_NAME];
    int age;
    struct person *next;
}person;

person * hash_table[TABLE_SIZE];

//hash function(gives a value to every name)
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
        } else {
            printf("\t%i\t", i);
            person *tmp = hash_table[i];
            while (tmp != NULL) {
                printf("%s - ", tmp->name);
                tmp = tmp->next;
            }
            printf("\n");
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
    p->next = hash_table[index];
    hash_table[index] = p;
    return true;
}

//find a person in the table by their name
person *hash_table_lookup ( char *name) {
    int index = hash(name);
    person *tmp = hash_table[index];
    while (tmp != NULL && strcmp(tmp->name, name) != 0) {
        tmp = tmp->next;
    }
    return tmp;
}

//delete name in table
person *hash_table_delete(char *name) {
    int index = hash(name);
    person *tmp = hash_table[index];
    person *prev = NULL;
    while (tmp != NULL && strcmp(tmp->name, name) != 0) {
        prev = tmp;
        tmp = tmp->next;
    }
    if (tmp == NULL) return NULL;
    if (prev == NULL) {
        //deleting the head
        hash_table[index] = tmp->next;
    } else {
        prev->next = tmp->next;
    }
    return tmp;
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
    person jb= {.name="JB", .age=35};
    person malcolm= {.name="Malcolm", .age=30};
    person jude= {.name="Jude", .age=48};
    person willem= {.name="Willem", .age=49};

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
    hash_table_insert(&jb);
    hash_table_insert(&malcolm);
    hash_table_insert(&jude);
    hash_table_insert(&willem);
    print_table();

    person *tmp = hash_table_lookup("Adam");

    if(tmp == NULL) {
        printf("Not found\n");
    } else {
        printf("Found %s\n", tmp->name);
    }

    return 0;

}