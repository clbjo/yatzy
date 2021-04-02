function getValue(element) {
    return parseInt(element.attributes['value'].value)
}


function getDiceImages() {
    diceImages = document.getElementsByClassName('dice')
    return diceImages = Array.prototype.slice.call(diceImages, 0);
}


const state = {
    kept: [false, false, false, false, false],

    toggleKept(dice) {
        value = getValue(dice)
        this.kept[value] = !this.kept[value]
        updateVisuals(this)
    },
}


function updateVisuals(state) {
    getDiceImages().forEach(dice => {
        value = getValue(dice)
        if (state.kept[value]) {
            dice.classList.add('kept')
        } else {
            dice.classList.remove('kept')
        }
    })
}


function rollAll() {
    getDiceImages().forEach(image => {
        value = getValue(image)
        if (!state.kept[value]) {
            result = Math.floor(Math.random() * 6) + 1
            image.src = `images/${result}.png`
        }
    })
}


function keep(dice) {
    state.toggleKept(dice)
}

