/*
GAME RULES:

- The game has 2 players, playing in rounds
- In each turn, a player rolls a dice as many times as he whishes. Each result get added to his ROUND score
- BUT, if the player rolls a 1, all his ROUND score gets lost. After that, it's the next player's turn
- The player can choose to 'Hold', which means that his ROUND score gets added to his GLBAL score. After that, it's the next player's turn
- The first player to reach 100 points on GLOBAL score wins the game

*/
var scores, roundScore, activePlayer, gamePlaying, previousRollDice1, previousRollDice2;

init();

document.querySelector('.btn-roll').addEventListener('click', function() {
    
    if(gamePlaying){

        // 1. Random Number
        var dice1 = Math.floor(Math.random() * 6) + 1;
        var dice2 = Math.floor(Math.random() * 6) + 1;
        
        // 2. Display Result 
        var dice1DOM = document.querySelector('.dice1');
        dice1DOM.style.display = 'block';
        dice1DOM.src = 'dice-' + dice1 + '.png';

        var dice2DOM = document.querySelector('.dice2');
        dice2DOM.style.display = 'block';
        dice2DOM.src = 'dice-' + dice2 + '.png';
        

        // 3. Update the round score IF the rolled number was NOT a 1
        if ((dice1 !== 1 && dice2 !== 1) && !(previousRollDice1 === 6 && dice1 === 6) && !(previousRollDice2 === 6 && dice2 === 6)) {
            // add score
            roundScore += dice1 + dice2;
            previousRollDice1 = dice1;
            previousRollDice2 = dice2;
            document.querySelector('#current-' + activePlayer).textContent = roundScore;
        } else {
            // Next player
            nextPlayer();

        }
    }

});


document.querySelector('.btn-hold').addEventListener('click', function() {

    if (gamePlaying){
        // Add CURRENT score to GLOBAL score
        scores[activePlayer] += roundScore; 

        // Update the UI
        document.querySelector('#score-' + activePlayer).textContent = scores[activePlayer];

        // Check if player won the game
        if (scores[activePlayer] >= document.querySelector('#game-score').value ) {
            document.querySelector('#name-' + activePlayer).textContent = 'Winner!';
            document.querySelector('.dice1').style.display = 'none';
            document.querySelector('.dice2').style.display = 'none';
            document.querySelector('.player-' + activePlayer + '-panel').classList.add('winner');
            document.querySelector('.player-' + activePlayer + '-panel').classList.remove('active');
            gamePlaying = false;
        } else {
            // Next player
            nextPlayer();
        }
    }

});

function nextPlayer () {
    // Next Player
    activePlayer === 0 ? activePlayer = 1 : activePlayer = 0;
    roundScore = 0;
    previousRoll = 0;

    document.getElementById('current-0').textContent = '0';
    document.getElementById('current-1').textContent = '0';

    document.querySelector('.player-0-panel').classList.toggle('active');
    document.querySelector('.player-1-panel').classList.toggle('active');

}

document.querySelector('.btn-new').addEventListener('click', init); 

function init() {

    scores = [0, 0];
    activePlayer = 0;
    roundScore = 0;
    gamePlaying = true;

    document.querySelector('.dice1').style.display = 'none';
    document.querySelector('.dice2').style.display = 'none';

    document.getElementById('score-0').textContent = '0';
    document.getElementById('score-1').textContent = '0';
    document.getElementById('current-0').textContent = '0';
    document.getElementById('current-0').textContent = '0';
    document.querySelector('#game-score').value = '100';

    document.querySelector('#name-0').textContent = 'Player 1';
    document.querySelector('#name-1').textContent = 'Player 2';
    document.querySelector('.player-0-panel').classList.remove('winner');
    document.querySelector('.player-1-panel').classList.remove('winner');
    document.querySelector('.player-0-panel').classList.remove('active');
    document.querySelector('.player-0-panel').classList.add('active');
    document.querySelector('.player-1-panel').classList.remove('active');

}

document.querySelector('.btn-inst').addEventListener('click', function() {
    alert('GAME RULES:\n- The game has 2 players, playing in rounds\n' + 
        '- In each turn, a player rolls two dice as many times as he/she wishes. Each result gets added to his/her current score\n' + 
'- BUT, if the player rolls a 1 or one of the dice rolls consecutive 6\'s, all his/her current score gets lost. After that, it\'s the next player\'s turn\n'+
'- The player can choose to \'Hold\', which means that his/her current score gets added to his/her total score. After that, it\'s the next player\'s turn\n'+
'- The first player to reach 100 points or the specified point total on total score wins the game');
});




