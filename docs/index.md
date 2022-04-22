# Problema de valor inicial

Este projeto realiza a solução numérica de uma equaçao diferencial, quando suas condições de contorno são satisfeitas.

## Método numérico

O método numérico que empregamos é o Runge Kutta de quarta ordem.

## exemplos de uso

Escrever uma função que retorne o valor da equaçao diferencial $\frac{dy}{dt}$, por exemplo:

$$
\frac{dy}{dt} = \sin{t} - ty
$$

```python
def f(t, y):
    return np.sin(t) - t * y
```
