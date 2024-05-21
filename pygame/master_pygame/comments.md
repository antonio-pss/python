# Guia PyGame

    pip install pygame-ce

### O que o PyGame faz?
- Criar imagens e Tocar Sons.
- Verificar ações do usuário.
- Pegar e setar posições.
- ...

### Por que usar PyGame?
Para aprender a resolver problemas!
PtGame não é completo, então aprender a usá-lo é aprender a resolver problemas que no futuro podem ser de muita experiência.

### Surfaces (Superfícies)
- Importar imagens e textos.
- Funciona como uma tela.
### Rectangles
- Posicionar superfícies.
- Fazer colisões.

### Loop
O jogo precisa rodar infinitamente. Para isso usamos um 'while True'.
Nesse loop, criamos elementos, verificamos ações, etc.

### Update x Flip
- Update atualiza tudo na tela.
- Flip atualiza apenas uma parte específicada.

### Blit
Colocar uma superfície em cima da outra.
`surface1.blit(surface2, (X, Y))`

### Plano Cartesiano da Tela
A posição original (0, 0) fica no canto superior esquerdo da tela. 
O Y é invertido, o positivo dele é para baixo.

### Frame Rate
A cada segundo o loop irá rodar algumas vezes.


