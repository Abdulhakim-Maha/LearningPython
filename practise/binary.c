#include<stdio.h>
int main(){
	int h,s,b,d,e,input;
	for(int i = 0;i < 32;i++){
		input = i;
		e = input % 2;
		input /= 2;
		d = input % 2;
		input /= 2;
		b = input % 2;
		input /= 2;
		s = input % 2;
		input /= 2;
		h = input % 2;
		input /= 2;
		printf("%d%d%d%d%d\n",h,s,b,d,e);
    }
}