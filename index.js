function getValue(element) {
    return parseInt(element.attributes['value'].value)
}


function getDiceImages() {
    diceImages = document.getElementsByClassName('dice')
    return diceImages = Array.prototype.slice.call(diceImages, 0);
}


const state = {
    values: [1, 1, 1, 1, 1],

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
        dice.src = `images/${state.values[diceNumber]}.png`
    })
}


function rollAll() {
    getDiceImages().forEach(image => {
        // all the dice images have a value corresponding to
        // their index in the state arrays
        diceNumber = getValue(image)
        if (!state.kept[diceNumber]) {
            state.values[diceNumber] = Math.floor(Math.random() * 6) + 1
        }
        updateVisuals(state)
    })
}


function keep(dice) {
    state.toggleKept(dice)
}

