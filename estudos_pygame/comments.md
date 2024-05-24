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
### Rectangles (Retângulos)
- Posicionar superfícies.
- Fazer colisões.
#### Rectangles Positions
- Base: top, bottom, right, left, center
- Junções: topleft, midbottom, bottomright, center
#### Float Rectangles
- Com FRects, podemos posicionar em pontos Float, como 100.245
- Por isso são muito mais precisos.
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
### Arquivos e Paths (Caminhos)
Em muitos sistemas operacionais o jeito de formar paths pode ser diferente.
Por isso podemos importar from `os.path import join`, com esse comando, podemos apenas dar o nome do arquivo.
`path = join('images', 'player.png')`
Assim seu código fica mais robusto e pode ser importado mais facílmente por outros.
### Convert() and Convert_Alpha()
As duas funções ajudam o pygame a trabalhar melhor com importações (Ex: Imagens).
A diferença é simples, com o `convert()`, se a imagem tiver fundo sem nada, ele preenche esse fundo.
Com o `convert_alpha()`, o fundo fica normal
### Vetores
Com vetores, podemos fazer 'tuplas' que podem ser usadas algébricamente.
Você também pode trabalhar apenas com posições x e y do vetor também.
`if right >= SCREEN_WIDTH or rect.left <= 0: direction.x *= -1`
Sendo 'direction' um vetor.
### Delta Time
Para podermos mexer algo sem se preocupar com o frame rate, usamos o delta time. Ele é = 1 / Frame Rate. 
Colocando ele para multiplicar com o movimento, conseguimos um movimento contínuo independente do Frame Rate.
Ex: `rect.center += direction * speed * delta`
Sendo 'direction' um vetor.
### Input 
- Event loop - Mousewheel, Touch...
- Classes - Pygame.Key; Pygame.Mouse...
### Normalize
`Direction = direction.normalize() if direction else direction`
- Essa linha permite fazer com que o jogador não dobre sua velocidade quando apertando duas teclas diferentes. Como Cima e Direita.
- Dentro do if, um vetor retornará false se ele for (0, 0). Se não, retorna True. Por fim, se direction == False, faça a linha, se não continue.
### Groups
- Podem desenhar (draw), atualizar (update) e organizar sprites.