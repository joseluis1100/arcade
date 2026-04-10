# Faça um programa para leia

Faça um programa para leia o horário (hora, minuto e segundo) de inicio e a duração, em segundos, de uma experiência biológica. O programa deve resultar com o novo horário (hora, minuto e segundo) do término da mesma.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int hora, minuto, segundo, duracao;
    scanf("%d %d %d %d", &hora, &minuto, &segundo, &duracao);

    int total_segundos = (hora * 3600) + (minuto * 60) + segundo + duracao;

    // Usamos o módulo 24 (% 24) para o caso de a experiência passar das 23:59:59 
    // e virar o dia. Se der 26 horas, o resultado volta para 2 horas da manhã!
    int h = (total_segundos / 3600) % 24;
    int m = (total_segundos % 3600) / 60;
    int s = total_segundos % 60;

    printf("%02d:%02d:%02d\n", h, m, s);

    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
10 30 0 3600
======== EXPECT
11:30:00
<<<<<<<< FINISH

>>>>>>>> INSERT
23 59 59 1
======== EXPECT
00:00:00
<<<<<<<< FINISH

>>>>>>>> INSERT
0 0 0 0
======== EXPECT
00:00:00
<<<<<<<< FINISH

>>>>>>>> INSERT
12 0 0 7200
======== EXPECT
14:00:00
<<<<<<<< FINISH

>>>>>>>> INSERT
8 30 45 5000
======== EXPECT
09:54:05
<<<<<<<< FINISH
```

[Código](./C/draft.c)
