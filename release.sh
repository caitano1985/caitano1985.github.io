#!/bin/bash
git status
git add .
read -p "Digite a mensagem do commit: " mensagem
git commit -m "$mensagem"
git push
echo "✅ Deploy concluído com sucesso!"#!/bin/bash
git status
git add .
read -p "Digite a mensagem do commit: " mensagem
git commit -m "$mensagem"
git push
echo "✅ Deploy concluído com sucesso!"
