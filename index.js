
function rollAll() {
    var diceImages = document.getElementsByClassName('dice')
    var diceImages = Array.prototype.slice.call(diceImages, 0 );
    diceImages.forEach(image => {
        let result = Math.floor(Math.random() * 6) + 1
        image.src = `images/${result}.png`
    })
}

