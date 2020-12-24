#include <iostream>
#include "a.h"
#include "b.h"

#g++ -o libab.so -fPIC -shared a.cpp b.cpp -I.
#g++ -o main mian.cpp -L. -lab

using namespace std;

int main()
{
	test t;
	t.function();
	
	cs s;
	s.function();
	return 0;
}
