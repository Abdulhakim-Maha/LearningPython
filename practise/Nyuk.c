#include <stdio.h>
void main(){
    int n;
    printf("Enter Input:");
    scanf("%d",&n);
    int arr[n][n];

    for(int r=0; r<n; r++){
        for(int c=0; c<n; c++){
            arr[r][c] =-1;
        }
    }
    int count=1;
    for(int i=0; i<n; i++){
        arr[i][0] =count%10;
        count++;
    }
    count =2;
    for(int i=1; i<n-1; i++){

        arr[i][i+0*i]=count%10;
        count++;
    }
    count=1;
    for(int i=0; i<n; i++){
        arr[i][n-1] =count%10;
        count++;
    }

    for(int r=0; r<n; r++){
        for(int c=0; c<n; c++){
        if(arr[r][c]==-1){
            printf(" ");
        }else{
            printf("%d",arr[r][c]);
        }



        }
        printf("\n");


    }

}
