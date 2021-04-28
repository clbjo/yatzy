function roomSelected() {
    select = document.getElementById('rooms')
    if (select.value == '') {
        // TODO
    } else {
        window.location.href = `/play/${select.value}`
    }
}