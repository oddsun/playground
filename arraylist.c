#include "arraylist.h"


ArrayList *arraylist_new(size_t el_size){
    ArrayList *list = malloc(sizeof(ArrayList));
    list->size = 0;
    list->capacity = 10;
    list->data = malloc(el_size * list->capacity);
    return list;
}

void arraylist_free(ArrayList *list){
    free(list->data);
    free(list);
}

void arraylist_add(ArrayList *list, void *el){
    if(list->size == list->capacity){
        list->capacity *= 2;
        list->data = realloc(list->data, list->capacity);
    }
    list->data[list->size++] = el;
}

void *arraylist_get(ArrayList *list, size_t index){
    if(index >= list->size){
        return NULL;
    }
    return list->data[index];
}

void arraylist_set(ArrayList *list, size_t index, void *el){
    if(index >= list->size){
        return;
    }
    list->data[index] = el;
}

void arraylist_remove(ArrayList *list, size_t index){
    if(index >= list->size){
        return;
    }
    for(size_t i = index; i < list->size - 1; i++){
        list->data[i] = list->data[i + 1];
    }
    list->size--;
}

size_t arraylist_size(ArrayList *list){
    return list->size;
}

size_t arraylist_capacity(ArrayList *list){
    return list->capacity;
}

void arraylist_clear(ArrayList *list){
    list->size = 0;
}

bool arraylist_contains(ArrayList *list, void *el, int(*cmp)(void *, void *)){
    for(size_t i = 0; i < list->size; i++){
        void *el_in_list = arraylist_get(list, i);
        if(cmp(el_in_list, el) == 0){
            return true;
        }
    }
    return false;
}