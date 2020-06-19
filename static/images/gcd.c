#include<stdio.h>
#include<conio.h>


int func_gcd(int num1, int num2)
{
    if(num1 >= num2)
    {
        int remainder = 0;
        remainder = num1 % num2;
        if(remainder == 0)
            return num2;

        else
            func_gcd(num2, remainder);
    }
    else
        func_gcd(num2, num1);
}

void main()

{
    int a[10] = {10, 7, 8, 9, 11};
    //scanf("%d %d", &a, &b);
    //printf("%d", func_gcd(a,b));

    for(int i; i<4; i++)
    {
        for(int j = i+1; j < 5; j++)
        {
            int hcf = func_gcd(a[i], a[j]);
            if(hcf == 1)
                printf("%4d %4d\n", a[i], a[j]);
        }
    }


}
