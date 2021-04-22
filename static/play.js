const IMAGES_URL = '/static/images'


//-------------------- SocketIO --------------------// 


const socket = io();

socket.on('connect', () => {
    socket.emit('join', document.URL)
});

socket.on('update', newState => {
    state = {...state, ...newState}
    updateVisuals(state)
})


//-------------------- Interface --------------------// 


function roll() {
    socket.emit('roll')
}

function keep(index) {
    socket.emit('keep', index)
}

function reset(index) {
    socket.emit('reset')
}


//-------------------- Visuals --------------------// 


function getIndex(element) {
    return parseInt(element.attributes['index'].value)
}


function getDiceImages() {
    diceImages = document.getElementsByClassName('dice')
    return diceImages = Array.prototype.slice.call(diceImages, 0);
}


let state = {}
function updateVisuals(state) {
    getDiceImages().forEach(dice => {
        diceNumber = getIndex(dice)
        if (state.kept[diceNumber]) {
            dice.classList.add('kept')
        } else {
            dice.classList.remove('kept')
        }
        dice.src = `${IMAGES_URL}/${state.values[diceNumber]}.png`
    })
    document.getElementById('throw-counter').textContent = state.counter
}
