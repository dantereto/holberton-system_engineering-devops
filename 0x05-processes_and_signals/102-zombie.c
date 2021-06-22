#include <unistd.h>
#include <stdio.h>
#include <stdio_ext.h>
#include <sys/types.h>
#include <sys/wait.h>
/**
 * infinite_while -  infinite_while
 *Return: return 0
 */
int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}
/**
 * main -  checks for uppercase character
 *Return: return 0
 */
int main(void)
{
pid_t pid = 0;
int i = 0;
for (i = 0; i < 5; i++)
{
pid = fork();
if (pid == 0)
{
printf("Zombie process created, PID: %d\n", getpid());
return (0);
}
}
infinite_while();
return (0);
}
