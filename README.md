# Josinfo: Network Architect

Crie um site de portfólio profissional, em português (pt-BR) e (IN-EUA), para Josimar Caitano ("Josinfo"), especialista sênior em redes e engenheiro de infraestrutura de TI.

## SOBRE A PESSOA

- Nome: Josimar Caitano da Silva

- Marca pessoal: Josinfo

- Certificação: CCIE x2 (Cisco Certified Internetwork Expert, dupla certificação)

- Cargo atual: Principal IP Solutions Architect for Financial Services

- Especialidades técnicas: roteamento avançado (OSPF e afins), segurança de rede, Network Operations Center (NOC), Cisco StealthWatch, arquitetura de soluções IP para o setor financeiro

- Atua como instrutor/mentor: dá aulas de CCNA DevNet e CCNP Encor, além de conduzir sessões práticas de preparação para o CCIE Lab (ex: sessões sobre OSPF)

- Produz conteúdo técnico: artigos tipo "HowTo" e vídeos explicativos sobre temas de rede e segurança

- Reconhecido pela comunidade (ex: Academia Brasileira de Redes - ABRedes) como referência em roteamento e mentoria técnica

## ESTILO VISUAL

Dark mode técnico, com estética inspirada em dashboards de rede / terminal:

- Fundo escuro (tons de grafite/azul-marinho profundo)

- Cor de destaque em azul-ciano ou verde-neon (remetendo a topologia de rede, terminais, status "online")

- Tipografia moderna e legível: uma sans-serif para textos e, opcionalmente, uma fonte monoespaçada para detalhes técnicos (ex: badges de certificação, trechos de código/CLI)

- Elementos gráficos sutis remetendo a redes: linhas conectando nós, ícones de roteador/switch, grid de fundo discreto

- Visual profissional e sério (não é um portfólio criativo/artístico) — precisa transmitir autoridade técnica e confiança

## ESTRUTURA / SEÇÕES (página inicial)

1. **Hero / Topo**

   - Nome e marca (Josimar Caitano — Josinfo)

   - Título/subtítulo: algo como "CCIE x2 | Principal IP Solutions Architect | Instrutor de Redes"

   - Foto ou placeholder de foto profissional

   - CTA para contato e para redes sociais/YouTube

2. **Sobre**

   - Breve bio resumindo trajetória, especialidade em redes financeiras, e paixão por ensinar

3. **Experiência Profissional**

   - Cargo atual: Principal IP Solutions Architect for Financial Services

   - Espaço para outras experiências (usar placeholders "Empresa X — Cargo — Período")

4. **Certificações**

   - Destaque para CCIE x2 (com selo/badge visual)

   - Espaço para outras certificações Cisco (placeholders)

5. **Ensino & Mentoria**

   - Cursos que ele ministra: CCNA DevNet e CCNP Encor

   - Sessões práticas de laboratório para CCIE (ex: OSPF)

   - Descrição curta de metodologia/abordagem didática

6. **Projetos** (seção de destaque na home, com cards que levam a páginas/rotas próprias)

   - Cada projeto deve ter um card na home (imagem/diagrama de capa, título, resumo curto, tags de tecnologia) que leva para uma **rota individual** (ex: `/projetos/dna-center`, `/projetos/multicast`)

   - Cada página de projeto individual deve conter: título, contexto/problema, tecnologias utilizadas, descrição da solução/arquitetura, diagramas ou imagens (placeholder), resultados/aprendizados, e botão "Voltar para Projetos"

   - **Projetos iniciais a incluir:**

     a. **Cisco DNA Center** — projeto envolvendo automação e gerenciamento de rede via Cisco DNA Center (SD-Access, políticas de rede, automação, monitoramento). Usar conteúdo placeholder detalhado sobre arquitetura/implementação até receber o conteúdo real.

     b. **Multicast Receiver e Sender** — projeto de configuração/implementação de multicast em rede (PIM, IGMP, sender e receiver), com placeholder para topologia e configurações.

   - **Estrutura escalável para novos projetos:** criar uma página de listagem `/projetos` que renderiza os cards dinamicamente a partir de uma lista/array de projetos (não hardcoded múltiplas vezes), para que seja fácil adicionar novos projetos no futuro apenas adicionando um novo item à lista (cada um gerando automaticamente sua própria rota/página)

7. **Conteúdo & Publicações**

   - Espaço para artigos técnicos (ex: guia sobre Cisco StealthWatch) e vídeos

   - Cards com placeholder para links de YouTube/blog/LinkedIn

8. **Contato**

   - Formulário simples de contato

   - Links para LinkedIn, YouTube e e-mail (usar placeholders até serem fornecidos)

## REQUISITOS TÉCNICOS

- Totalmente responsivo (mobile-first)

- Roteamento com páginas/rotas independentes para cada projeto (estrutura tipo React Router ou equivalente), permitindo compartilhar o link direto de um projeto específico

- Estrutura de dados de projetos centralizada (array/lista de objetos) para facilitar adição de novos projetos sem duplicar código

- Navegação suave entre seções da home (scroll suave / âncoras) e navegação clara entre home e páginas de projeto

- Micro-interações discretas (hover states, transições suaves) sem exagerar

- Performance: imagens otimizadas, carregamento rápido

- Usar dados placeholder claramente identificáveis onde eu ainda não tiver fornecido conteúdo real (fotos, links, textos de experiência, diagramas de projeto)

This project was built with [Lovable](https://lovable.dev).

## Build with Lovable

Continue developing this project in the [Lovable editor](https://lovable.dev/projects/43f05882-ddea-4da3-a8d9-ab34501add48).

- **Ship faster**: describe what you want to build and Lovable handles the code.
- **Stay in sync**: every change made in Lovable is committed straight to this repository.
- **Full ownership**: this code is yours. Push to `main` on GitHub and your changes sync back into Lovable, ready for your next prompt.

## Development

Prefer working locally? You need Node.js and npm — [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating).

```sh
git clone <this-repository-url>
cd <repository-name>
npm i
npm run dev
```
