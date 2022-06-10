function DecNumber() {
    var result = document.getElementById('quantity');
    var qty = result.value;
    if (!isNaN(qty))
        result.value--;
    return false;
}

function IncreNumber() {
    var result = document.getElementById('quantity');
    var qty = result.value;
    if (!isNaN(qty))
        result.value++;
    return false;
}