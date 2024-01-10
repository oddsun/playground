#ifndef ARRAYLIST_H
#define ARRAYLIST_H

#include <stdlib.h>

/**
 * Struct for ArrayList.
 * size: Current size of the ArrayList.
 * capacity: Total capacity of the ArrayList.
 * data: Pointer to the data in the ArrayList.
 */
typedef struct ArrayList {
    size_t size;
    size_t capacity;
    void **data;
} ArrayList;

/**
 * Function to create a new ArrayList.
 * el_size: Size of the elements to be stored in the ArrayList.
 * Returns a pointer to the new ArrayList.
 */
ArrayList *arraylist_new(size_t el_size);

/**
 * Function to free an ArrayList.
 * list: The ArrayList to be freed.
 */
void arraylist_free(ArrayList *list);

/**
 * Function to add an element to the ArrayList.
 * list: The ArrayList to add the element to.
 * el: The element to be added.
 */
void arraylist_add(ArrayList *list, void *el);

/**
 * Function to get an element from the ArrayList.
 * list: The ArrayList to get the element from.
 * index: The index of the element to get.
 * Returns a pointer to the element.
 */
void *arraylist_get(ArrayList *list, size_t index);

/**
 * Function to set an element in the ArrayList.
 * list: The ArrayList to set the element in.
 * index: The index of the element to set.
 * el: The new element.
 */
void arraylist_set(ArrayList *list, size_t index, void *el);

/**
 * Function to remove an element from the ArrayList.
 * list: The ArrayList to remove the element from.
 * index: The index of the element to remove.
 */
void arraylist_remove(ArrayList *list, size_t index);

/**
 * Function to get the size of the ArrayList.
 * list: The ArrayList to get the size of.
 * Returns the size of the ArrayList.
 */
size_t arraylist_size(ArrayList *list);

/**
 * Function to get the capacity of the ArrayList.
 * list: The ArrayList to get the capacity of.
 * Returns the capacity of the ArrayList.
 */
size_t arraylist_capacity(ArrayList *list);

/**
 * Function to clear the ArrayList.
 * list: The ArrayList to clear.
 */
void arraylist_clear(ArrayList *list);

#endif // ARRAYLIST_H