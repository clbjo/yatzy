const STATIC_URL = '/static'


function getIndex(element) {
    return parseInt(element.attributes['index'].value)
}


function getDiceImages() {
    diceImages = document.getElementsByClassName('dice')
    return diceImages = Array.prototype.slice.call(diceImages, 0);
}


let state = {
    values: [1, 1, 1, 1, 1],

    counter: 0,

    kept: [false, false, false, false, false],

    toggleKept(dice) {
        value = getIndex(dice)
        this.kept[value] = !this.kept[value]
        updateVisuals(this)
    },
}


function updateVisuals(state) {
    getDiceImages().forEach(dice => {
        diceNumber = getIndex(dice)
        if (state.kept[diceNumber]) {
            dice.classList.add('kept')
        } else {
            dice.classList.remove('kept')
        }
        dice.src = `${STATIC_URL}/images/${state.values[diceNumber]}.png`
    })
    document.getElementById('throw-counter').innerHTML = state.counter
}


function nextPlayer() {
    state.counter = 0
    state.kept = [false, false, false, false, false]
    updateVisuals(state)
}


function rollAll() {
    getDiceImages().forEach(image => {
        // all the dice images have a value corresponding to
        // their index in the state arrays
        diceNumber = getIndex(image)
        if (!state.kept[diceNumber]) {
            state.values[diceNumber] = Math.floor(Math.random() * 6) + 1
        }
    })
    state.counter += 1
    updateVisuals(state)
}


function keep(dice) {
    state.toggleKept(dice)
}


//-------------------- SocketIO --------------------// 


// Emittable events
const JOIN = 'join'
const ACTION = 'action'

const socket = io();

socket.on('connect', () => {
    socket.emit(JOIN, document.URL)
});

socket.on('update', newState => {
    state = {...state, ...newState}
    updateVisuals(state)
})
