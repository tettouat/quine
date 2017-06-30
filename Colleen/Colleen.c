#include <stdio.h>
void f(void){
char *str = "#include <stdio.h>%cvoid f(void){%cchar *str = %c%s%c;%cprintf(str, 10, 10, 34, str, 34, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10);%c}%c/*%c    commentaire1%c*/%cint main(void){%c/*%c    commentaire2%c*/%cf();%creturn 0;%c}%c";
printf(str, 10, 10, 34, str, 34, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10);
}
/*
    commentaire1
*/
int main(void){
/*
    commentaire2
*/
f();
return 0;
}
