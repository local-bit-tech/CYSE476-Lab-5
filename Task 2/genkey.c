#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define KEYSIZE 16
void main()
{
    int i;

    //time from start to finish of interval where key is 
    long long start_time = 1524013729;
    long long end_time = 1524020929;


    char key[KEYSIZE];

    //loop through the time from start to finish generating a key
    for (start_time; start_time <= end_time; start_time++){
        //seed a new number from each time
        srand(start_time);
        for (i = 0; i < KEYSIZE; i++){
            key[i] = rand()%256;
            printf("%.2x", (unsigned char)key[i]);
        }
        printf("\n");
    }
}

