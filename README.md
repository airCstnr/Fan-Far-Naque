# discord-bot-template

Template de bot Discord.

## Lancement

Pour lancer le bot, se munir du token du bot, et le lancer avec la commande :
```
python3 main.py $TOKEN
```

## Extension

Pour ajouter une action au bot, creer un nouveau fichier Python dans le package `actions` et y creer une
classe heritant de `actions.AbstractAction` (voir la documentation dans `action.py` pour savoir ce que fait
chaque methode, l'action `actions.Help` peut etre prise comme exemple)

Une fois la classe implementee, ajouter l'action avec `ActionList.add_action(<classe>)` au debut de
`main.py`
