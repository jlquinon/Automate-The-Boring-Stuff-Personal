#! /usr/bin/env python3

import zombiedice

class JorgeZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        '''
        Roll as long as much as we can (incredibly greedy approach)
        '''

        shotguns = 0
        brains = 0
        while shotguns < 2:
            results = zombiedice.roll()

            if not results:
                print('No results in Jorge Zombie')
                return
            
            shotguns += results['shotgun']
            brains += results['brains']


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    zombiedice.examples.MinNumShotgunsThenStopsOneMoreZombie(name='Stop at 2 Shotguns then one more', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsOneMoreZombie(name='Stop at 1 Shotgun then one more', minShotguns=1),
    zombiedice.examples.MonteCarloZombie(name='Monte Carlo', riskiness=40, numExperiments=20),
    # Add any other zombie players here.
    JorgeZombie(name='Jorge Zombie Bot')
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)