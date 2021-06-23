#include <stdio.h>
#include <stdlib.h>

int modify(int k) {
  int x = k;
  while (x > 13) {
    x -= 13;
  }

  return x;
}


int * create_deck () {
  int deck[52];
  for (int i = 1; i <53; i++) {
    deck[i] = takeaway(i);
  }
  return deck;
}

int shuffle () {
  time_t t;
  
  srand((unsigned) time(&t));
  
  for( i = 0 ; i < n ; i++ ) {
      printf("%d\n", rand() % 50);
   }
   return 0;
}


int main() {
  int[] deck = create_deck();
  for (int i = 0; i <52; i++) {
    printf("%d", deck[i])  
  }
  shuffle();

  return 0;
}
