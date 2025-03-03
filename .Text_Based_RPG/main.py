import config
from reference.playerDict import player
from reference.actions.forage import search
from reference.actions import inBattle


class RPG:
    player.characterCreation()
    search()
    inBattle.battle.startBattle(config.opponent, config.user)