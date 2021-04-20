function getValue(element) {
    return parseInt(element.attributes['value'].value)
}


function getDiceImages() {
    diceImages = document.getElementsByClassName('dice')
    return diceImages = Array.prototype.slice.call(diceImages, 0);
}


let state = {
    values: [1, 1, 1, 1, 1],

    throwCounter: 0,

    kept: [false, false, false, false, false],

    toggleKept(dice) {
        value = getValue(dice)
        this.kept[value] = !this.kept[value]
        updateVisuals(this)
    },
}


function updateVisuals(state) {
    getDiceImages().forEach(dice => {
        diceNumber = getValue(dice)
        if (state.kept[diceNumber]) {
            dice.classList.add('kept')
        } else {
            dice.classList.remove('kept')
        }
        dice.src = `static/images/${state.values[diceNumber]}.png`
    })
    document.getElementById('throw-counter').innerHTML = state.throwCounter
}


function nextPlayer() {
    state.throwCounter = 0
    state.kept = [false, false, false, false, false]
    updateVisuals(state)
}


function rollAll() {
    getDiceImages().forEach(image => {
        // all the dice images have a value corresponding to
        // their index in the state arrays
        diceNumber = getValue(image)
        if (!state.kept[diceNumber]) {
            state.values[diceNumber] = Math.floor(Math.random() * 6) + 1
        }
    })
    state.throwCounter += 1
    updateVisuals(state)
}


function keep(dice) {
    state.toggleKept(dice)
}


//-------------------- SocketIO --------------------// 


const socket = io();

socket.on('connect', () => {
    socket.emit('greeting')
    socket.emit('action', 'roll')
});

socket.on('update', newState => {
    state = {...state, ...newState}
    updateVisuals(state)
})

