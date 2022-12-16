#include<stdio.h>
int main(){
	//ประกาศตัวแปร
	int id;
	char name[20]; // austiniqer
	float salary;

	//รับค่าจาก user
	printf("Enter your id: ");
	scanf("%d",&id);
	printf("Enter your name: ");
	scanf("%s",&name);
	printf("Enter your salary: ");
	scanf("%f",&salary);

	// printf("%d %s %.3f",id,name,salary);
	if(salary > 50000){
		salary = salary - salary*0.1;
	}else{
		salary = salary - salary*0.05;	
	}
	printf("Your salary is %.3f",salary);

}